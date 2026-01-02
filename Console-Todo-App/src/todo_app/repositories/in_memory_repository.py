"""
In-Memory Repository

This module implements an in-memory repository for storing todo items.
"""
from typing import List, Optional
from src.todo_app.models.todo import Todo


class TodoRepository:
    """
    In-memory repository for todo items.
    """
    def __init__(self):
        self._todos: List[Todo] = []
        self._next_id = 1

    def add(self, todo: Todo) -> Todo:
        """
        Add a new todo to the repository.

        Args:
            todo: The todo item to add

        Returns:
            The added todo item with updated ID
        """
        todo.id = self._next_id
        self._next_id += 1
        self._todos.append(todo)
        return todo

    def get_all(self) -> List[Todo]:
        """
        Get all todos from the repository.

        Returns:
            List of all todo items
        """
        return self._todos.copy()

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The todo item if found, None otherwise
        """
        for todo in self._todos:
            if todo.id == todo_id:
                return todo
        return None

    def update(self, todo_id: int, title: str = None, completed: bool = None) -> Optional[Todo]:
        """
        Update a todo item.

        Args:
            todo_id: The ID of the todo to update
            title: New title (optional)
            completed: New completion status (optional)

        Returns:
            The updated todo if found, None otherwise
        """
        todo = self.get_by_id(todo_id)
        if todo is None:
            return None

        if title is not None:
            todo.update_title(title)
        if completed is not None:
            if completed:
                todo.mark_complete()
            else:
                todo.mark_incomplete()

        return todo

    def delete(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was deleted, False if not found
        """
        for i, todo in enumerate(self._todos):
            if todo.id == todo_id:
                del self._todos[i]
                return True
        return False