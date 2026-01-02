"""
Main Application Entry Point

This module provides the main entry point for the console todo application.
"""
from src.todo_app.repositories.in_memory_repository import TodoRepository
from src.todo_app.services.todo_service import TodoService
from src.todo_app.cli.cli_controller import CLIController


def main():
    """
    Main entry point for the console todo application.
    """
    # Initialize the application components
    repository = TodoRepository()
    service = TodoService(repository)
    controller = CLIController(service)

    print("Welcome to the Console Todo App!")
    print("Type 'help' for available commands or 'exit' to quit.")

    # Start the CLI loop
    controller.run()


if __name__ == "__main__":
    main()