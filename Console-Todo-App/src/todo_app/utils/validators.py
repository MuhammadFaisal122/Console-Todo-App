"""
Validation Utilities

This module provides validation functions for the todo application.
"""


def validate_todo_title(title: str) -> bool:
    """
    Validate a todo title.

    Args:
        title: The title to validate

    Returns:
        True if the title is valid, False otherwise
    """
    if not title or not title.strip():
        return False
    if len(title.strip()) > 255:  # Reasonable length limit
        return False
    return True


def validate_todo_id(todo_id: int) -> bool:
    """
    Validate a todo ID.

    Args:
        todo_id: The ID to validate

    Returns:
        True if the ID is valid, False otherwise
    """
    if not isinstance(todo_id, int):
        return False
    if todo_id <= 0:
        return False
    return True


def format_todo_list(todos) -> str:
    """
    Format a list of todos for display.

    Args:
        todos: List of todo items to format

    Returns:
        Formatted string representation of the todo list
    """
    if not todos:
        return "No todos found."

    output = []
    output.append("ID  | Completed | Title")
    output.append("--- | --------- | -----")

    for todo in todos:
        status = "X" if todo.completed else "O"
        output.append(f"{todo.id:3d} | {status:^9} | {todo.title}")

    return "\n".join(output)