"""
CLI Controller

This module provides the command-line interface for the todo application.
"""
from typing import Optional
from src.todo_app.services.todo_service import TodoService
from src.todo_app.utils.validators import validate_todo_title, format_todo_list


class CLIController:
    """
    Controller for handling CLI commands.
    """
    def __init__(self, service: TodoService):
        self.service = service

    def run(self):
        """
        Run the main CLI loop.
        """
        while True:
            try:
                command = input("\ntodo> ").strip().lower()

                if command == "exit" or command == "quit":
                    print("Goodbye!")
                    break
                elif command == "help":
                    self._show_help()
                elif command.startswith("add "):
                    self._handle_add(command[4:].strip())
                elif command == "list" or command == "view":
                    self._handle_view()
                elif command.startswith("update "):
                    self._handle_update(command[7:].strip())
                elif command.startswith("delete "):
                    self._handle_delete(command[7:].strip())
                elif command.startswith("complete "):
                    self._handle_complete(command[9:].strip())
                elif command.startswith("incomplete "):
                    self._handle_incomplete(command[11:].strip())
                else:
                    print(f"Unknown command: {command}. Type 'help' for available commands.")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

    def _show_help(self):
        """
        Show help information.
        """
        help_text = """
Available commands:
  add <title>        - Add a new todo with the given title
  list/view          - Show all todos
  update <id> <new_title> - Update the title of a todo by ID
  delete <id>        - Delete a todo by ID
  complete <id>      - Mark a todo as complete by ID
  incomplete <id>    - Mark a todo as incomplete by ID
  help               - Show this help message
  exit/quit          - Exit the application
        """
        print(help_text.strip())

    def _handle_add(self, args: str):
        """
        Handle the add command.
        """
        if not args:
            print("Usage: add <title>")
            return

        if not validate_todo_title(args):
            print("Error: Invalid title. Title must not be empty and should be less than 255 characters.")
            return

        try:
            todo = self.service.add_todo(args)
            print(f"Added todo: '{todo.title}' (ID: {todo.id})")
        except Exception as e:
            print(f"Error adding todo: {e}")

    def _handle_view(self):
        """
        Handle the view/list command.
        """
        try:
            todos = self.service.get_all_todos()
            formatted_list = format_todo_list(todos)
            print(formatted_list)
        except Exception as e:
            print(f"Error viewing todos: {e}")

    def _handle_update(self, args: str):
        """
        Handle the update command.
        """
        if not args:
            print("Usage: update <id> <new_title>")
            return

        parts = args.split(" ", 1)
        if len(parts) != 2:
            print("Usage: update <id> <new_title>")
            return

        try:
            todo_id = int(parts[0])
            new_title = parts[1]

            if not validate_todo_title(new_title):
                print("Error: Invalid title. Title must not be empty and should be less than 255 characters.")
                return

            todo = self.service.update_todo(todo_id, new_title)
            if todo:
                print(f"Updated todo (ID: {todo.id}) to: '{todo.title}'")
            else:
                print(f"Todo with ID {todo_id} not found.")
        except ValueError:
            print("Error: ID must be a number.")
        except Exception as e:
            print(f"Error updating todo: {e}")

    def _handle_delete(self, args: str):
        """
        Handle the delete command.
        """
        if not args:
            print("Usage: delete <id>")
            return

        try:
            todo_id = int(args)
            success = self.service.delete_todo(todo_id)
            if success:
                print(f"Deleted todo with ID {todo_id}")
            else:
                print(f"Todo with ID {todo_id} not found.")
        except ValueError:
            print("Error: ID must be a number.")
        except Exception as e:
            print(f"Error deleting todo: {e}")

    def _handle_complete(self, args: str):
        """
        Handle the complete command.
        """
        if not args:
            print("Usage: complete <id>")
            return

        try:
            todo_id = int(args)
            todo = self.service.mark_complete(todo_id)
            if todo:
                print(f"Marked todo (ID: {todo.id}) as complete: '{todo.title}'")
            else:
                print(f"Todo with ID {todo_id} not found.")
        except ValueError:
            print("Error: ID must be a number.")
        except Exception as e:
            print(f"Error marking todo as complete: {e}")

    def _handle_incomplete(self, args: str):
        """
        Handle the incomplete command.
        """
        if not args:
            print("Usage: incomplete <id>")
            return

        try:
            todo_id = int(args)
            todo = self.service.mark_incomplete(todo_id)
            if todo:
                print(f"Marked todo (ID: {todo.id}) as incomplete: '{todo.title}'")
            else:
                print(f"Todo with ID {todo_id} not found.")
        except ValueError:
            print("Error: ID must be a number.")
        except Exception as e:
            print(f"Error marking todo as incomplete: {e}")