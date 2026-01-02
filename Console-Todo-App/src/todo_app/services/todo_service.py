"""
Todo Service

This module provides business logic for todo operations.
"""
from typing import List, Optional
from src.todo_app.models.todo import Todo
from src.todo_app.repositories.in_memory_repository import TodoRepository


class TodoService:
    """
    Service layer for todo operations.
    """
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def add_todo(self, title: str) -> Todo:
        """
        Add a new todo item.

        Args:
            title: The title of the new todo item

        Returns:
            The created todo item
        """
        from datetime import datetime
        todo = Todo(
            id=0,  # Will be set by repository
            title=title,
            completed=False,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        return self.repository.add(todo)

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todo items.

        Returns:
            List of all todo items
        """
        return self.repository.get_all()

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Get a todo item by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The todo item if found, None otherwise
        """
        return self.repository.get_by_id(todo_id)

    def update_todo(self, todo_id: int, title: str = None) -> Optional[Todo]:
        """
        Update a todo item's title.

        Args:
            todo_id: The ID of the todo to update
            title: The new title (optional)

        Returns:
            The updated todo if found, None otherwise
        """
        return self.repository.update(todo_id, title=title)

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was deleted, False if not found
        """
        return self.repository.delete(todo_id)

    def mark_complete(self, todo_id: int) -> Optional[Todo]:
        """
        Mark a todo as complete.

        Args:
            todo_id: The ID of the todo to mark complete

        Returns:
            The updated todo if found, None otherwise
        """
        return self.repository.update(todo_id, completed=True)

    def mark_incomplete(self, todo_id: int) -> Optional[Todo]:
        """
        Mark a todo as incomplete.

        Args:
            todo_id: The ID of the todo to mark incomplete

        Returns:
            The updated todo if found, None otherwise
        """
        return self.repository.update(todo_id, completed=False)