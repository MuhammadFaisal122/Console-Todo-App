import unittest
from src.todo_app.services.todo_service import TodoService
from src.todo_app.repositories.in_memory_repository import TodoRepository
from src.todo_app.models.todo import Todo
from datetime import datetime


class TestTodoService(unittest.TestCase):
    """Unit tests for the TodoService."""

    def setUp(self):
        """Set up a fresh service with repository for each test."""
        self.repo = TodoRepository()
        self.service = TodoService(self.repo)

    def test_add_todo(self):
        """Test adding a todo through the service."""
        todo = self.service.add_todo("Test todo")
        self.assertIsNotNone(todo)
        self.assertEqual(todo.title, "Test todo")
        self.assertFalse(todo.completed)

    def test_get_all_todos_empty(self):
        """Test getting all todos when repository is empty."""
        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 0)

    def test_get_all_todos(self):
        """Test getting all todos through the service."""
        # Add some todos
        self.service.add_todo("Todo 1")
        self.service.add_todo("Todo 2")

        todos = self.service.get_all_todos()
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0].title, "Todo 1")
        self.assertEqual(todos[1].title, "Todo 2")

    def test_get_todo_by_id_found(self):
        """Test getting a todo by ID through the service."""
        added_todo = self.service.add_todo("Test todo")
        retrieved_todo = self.service.get_todo_by_id(added_todo.id)
        self.assertIsNotNone(retrieved_todo)
        self.assertEqual(retrieved_todo.id, added_todo.id)
        self.assertEqual(retrieved_todo.title, "Test todo")

    def test_get_todo_by_id_not_found(self):
        """Test getting a todo by ID that doesn't exist."""
        todo = self.service.get_todo_by_id(999)
        self.assertIsNone(todo)

    def test_update_todo(self):
        """Test updating a todo through the service."""
        added_todo = self.service.add_todo("Original title")
        updated_todo = self.service.update_todo(added_todo.id, "Updated title")
        self.assertIsNotNone(updated_todo)
        self.assertEqual(updated_todo.title, "Updated title")

    def test_update_todo_not_found(self):
        """Test updating a todo that doesn't exist."""
        updated_todo = self.service.update_todo(999, "Updated title")
        self.assertIsNone(updated_todo)

    def test_delete_todo(self):
        """Test deleting a todo through the service."""
        added_todo = self.service.add_todo("Test todo")
        result = self.service.delete_todo(added_todo.id)
        self.assertTrue(result)

        # Verify it's gone
        retrieved_todo = self.service.get_todo_by_id(added_todo.id)
        self.assertIsNone(retrieved_todo)

    def test_delete_todo_not_found(self):
        """Test deleting a todo that doesn't exist."""
        result = self.service.delete_todo(999)
        self.assertFalse(result)

    def test_mark_complete(self):
        """Test marking a todo as complete through the service."""
        added_todo = self.service.add_todo("Test todo")
        self.assertFalse(added_todo.completed)

        completed_todo = self.service.mark_complete(added_todo.id)
        self.assertIsNotNone(completed_todo)
        self.assertTrue(completed_todo.completed)

    def test_mark_complete_not_found(self):
        """Test marking a todo as complete when it doesn't exist."""
        completed_todo = self.service.mark_complete(999)
        self.assertIsNone(completed_todo)

    def test_mark_incomplete(self):
        """Test marking a todo as incomplete through the service."""
        added_todo = self.service.add_todo("Test todo")
        completed_todo = self.service.mark_complete(added_todo.id)
        self.assertTrue(completed_todo.completed)

        incomplete_todo = self.service.mark_incomplete(added_todo.id)
        self.assertIsNotNone(incomplete_todo)
        self.assertFalse(incomplete_todo.completed)

    def test_mark_incomplete_not_found(self):
        """Test marking a todo as incomplete when it doesn't exist."""
        incomplete_todo = self.service.mark_incomplete(999)
        self.assertIsNone(incomplete_todo)


if __name__ == '__main__':
    unittest.main()