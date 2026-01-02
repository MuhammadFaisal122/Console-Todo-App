import unittest
from src.todo_app.models.todo import Todo
from datetime import datetime


class TestTodoModel(unittest.TestCase):
    """Unit tests for the Todo model."""

    def test_create_todo(self):
        """Test creating a todo with required attributes."""
        todo = Todo(id=1, title="Test todo", completed=False)
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test todo")
        self.assertFalse(todo.completed)

    def test_create_todo_defaults(self):
        """Test creating a todo with default values."""
        todo = Todo(id=1, title="Test todo")
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.title, "Test todo")
        self.assertFalse(todo.completed)

    def test_mark_complete(self):
        """Test marking a todo as complete."""
        todo = Todo(id=1, title="Test todo", completed=False)
        todo.mark_complete()
        self.assertTrue(todo.completed)

    def test_mark_incomplete(self):
        """Test marking a todo as incomplete."""
        todo = Todo(id=1, title="Test todo", completed=True)
        todo.mark_incomplete()
        self.assertFalse(todo.completed)

    def test_update_title(self):
        """Test updating a todo's title."""
        todo = Todo(id=1, title="Test todo", completed=False)
        todo.update_title("Updated title")
        self.assertEqual(todo.title, "Updated title")

    def test_timestamps(self):
        """Test that timestamps are set correctly."""
        created_at = datetime.now()
        todo = Todo(id=1, title="Test todo", completed=False, created_at=created_at)
        self.assertEqual(todo.created_at, created_at)
        self.assertIsNotNone(todo.updated_at)


if __name__ == '__main__':
    unittest.main()