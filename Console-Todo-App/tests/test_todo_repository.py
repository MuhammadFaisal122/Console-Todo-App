import unittest
from src.todo_app.models.todo import Todo
from src.todo_app.repositories.in_memory_repository import TodoRepository
from datetime import datetime


class TestTodoRepository(unittest.TestCase):
    """Unit tests for the TodoRepository."""

    def setUp(self):
        """Set up a fresh repository for each test."""
        self.repo = TodoRepository()

    def test_add_todo(self):
        """Test adding a todo to the repository."""
        todo = Todo(id=0, title="Test todo", completed=False, created_at=datetime.now(), updated_at=datetime.now())
        added_todo = self.repo.add(todo)
        self.assertEqual(added_todo.id, 1)
        self.assertEqual(added_todo.title, "Test todo")
        self.assertFalse(added_todo.completed)

    def test_get_all_todos_empty(self):
        """Test getting all todos when repository is empty."""
        todos = self.repo.get_all()
        self.assertEqual(len(todos), 0)

    def test_get_all_todos(self):
        """Test getting all todos from repository."""
        # Add some todos
        todo1 = Todo(id=0, title="Todo 1", completed=False, created_at=datetime.now(), updated_at=datetime.now())
        todo2 = Todo(id=0, title="Todo 2", completed=True, created_at=datetime.now(), updated_at=datetime.now())
        self.repo.add(todo1)
        self.repo.add(todo2)

        todos = self.repo.get_all()
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0].title, "Todo 1")
        self.assertEqual(todos[1].title, "Todo 2")

    def test_get_by_id_found(self):
        """Test getting a todo by ID that exists."""
        todo = Todo(id=0, title="Test todo", completed=False, created_at=datetime.now(), updated_at=datetime.now())
        added_todo = self.repo.add(todo)

        retrieved_todo = self.repo.get_by_id(added_todo.id)
        self.assertIsNotNone(retrieved_todo)
        self.assertEqual(retrieved_todo.id, added_todo.id)
        self.assertEqual(retrieved_todo.title, "Test todo")

    def test_get_by_id_not_found(self):
        """Test getting a todo by ID that doesn't exist."""
        todo = self.repo.get_by_id(999)
        self.assertIsNone(todo)

    def test_update_todo_title(self):
        """Test updating a todo's title."""
        todo = Todo(id=0, title="Original title", completed=False, created_at=datetime.now(), updated_at=datetime.now())
        added_todo = self.repo.add(todo)

        updated_todo = self.repo.update(added_todo.id, title="Updated title")
        self.assertIsNotNone(updated_todo)
        self.assertEqual(updated_todo.title, "Updated title")

    def test_update_todo_completed(self):
        """Test updating a todo's completion status."""
        todo = Todo(id=0, title="Test todo", completed=False, created_at=datetime.now(), updated_at=datetime.now())
        added_todo = self.repo.add(todo)

        updated_todo = self.repo.update(added_todo.id, completed=True)
        self.assertIsNotNone(updated_todo)
        self.assertTrue(updated_todo.completed)

    def test_update_todo_both(self):
        """Test updating both title and completion status."""
        todo = Todo(id=0, title="Original", completed=False, created_at=datetime.now(), updated_at=datetime.now())
        added_todo = self.repo.add(todo)

        updated_todo = self.repo.update(added_todo.id, title="Updated", completed=True)
        self.assertIsNotNone(updated_todo)
        self.assertEqual(updated_todo.title, "Updated")
        self.assertTrue(updated_todo.completed)

    def test_update_todo_not_found(self):
        """Test updating a todo that doesn't exist."""
        updated_todo = self.repo.update(999, title="Updated")
        self.assertIsNone(updated_todo)

    def test_delete_todo(self):
        """Test deleting a todo."""
        todo = Todo(id=0, title="Test todo", completed=False, created_at=datetime.now(), updated_at=datetime.now())
        added_todo = self.repo.add(todo)

        result = self.repo.delete(added_todo.id)
        self.assertTrue(result)

        # Verify it's gone
        retrieved_todo = self.repo.get_by_id(added_todo.id)
        self.assertIsNone(retrieved_todo)

    def test_delete_todo_not_found(self):
        """Test deleting a todo that doesn't exist."""
        result = self.repo.delete(999)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()