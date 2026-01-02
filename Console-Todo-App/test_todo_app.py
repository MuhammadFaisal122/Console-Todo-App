#!/usr/bin/env python3
"""
Test script for the Todo App functionality
"""
import sys
import os

def test_todo_app():
    """Test the todo application functionality"""
    print("Testing Todo Application...")

    # Add the src directory to Python path
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

    # Import the application components
    try:
        from src.todo_app.repositories.in_memory_repository import TodoRepository
        from src.todo_app.services.todo_service import TodoService
        from src.todo_app.cli.cli_controller import CLIController
        print("[OK] Successfully imported all components")
    except ImportError as e:
        print(f"[ERROR] Import error: {e}")
        return False

    # Test repository functionality
    print("\nTesting Repository...")
    repo = TodoRepository()

    # Test adding a todo
    from src.todo_app.models.todo import Todo
    from datetime import datetime
    todo = Todo(id=0, title="Test todo", completed=False, created_at=datetime.now(), updated_at=datetime.now())
    added_todo = repo.add(todo)
    print(f"[OK] Added todo: ID {added_todo.id}, Title: {added_todo.title}")

    # Test getting all todos
    todos = repo.get_all()
    print(f"[OK] Retrieved {len(todos)} todos")

    # Test getting by ID
    retrieved_todo = repo.get_by_id(added_todo.id)
    if retrieved_todo:
        print(f"[OK] Retrieved todo by ID: {retrieved_todo.title}")
    else:
        print("[ERROR] Failed to retrieve todo by ID")
        return False

    # Test updating a todo
    updated_todo = repo.update(added_todo.id, title="Updated test todo", completed=True)
    if updated_todo and updated_todo.title == "Updated test todo" and updated_todo.completed:
        print(f"[OK] Updated todo: {updated_todo.title}, Completed: {updated_todo.completed}")
    else:
        print("[ERROR] Failed to update todo")
        return False

    # Test deleting a todo
    deleted = repo.delete(added_todo.id)
    if deleted:
        print("[OK] Deleted todo successfully")
    else:
        print("[ERROR] Failed to delete todo")
        return False

    # Test service functionality
    print("\nTesting Service...")
    service = TodoService(repo)

    # Test adding via service
    service_todo = service.add_todo("Service test todo")
    print(f"[OK] Service added todo: ID {service_todo.id}, Title: {service_todo.title}")

    # Test getting all via service
    all_todos = service.get_all_todos()
    print(f"[OK] Service retrieved {len(all_todos)} todos")

    # Test updating via service
    updated_via_service = service.update_todo(service_todo.id, "Updated via service")
    if updated_via_service and updated_via_service.title == "Updated via service":
        print(f"[OK] Service updated todo: {updated_via_service.title}")
    else:
        print("[ERROR] Service failed to update todo")
        return False

    # Test marking complete/incomplete via service
    completed_todo = service.mark_complete(service_todo.id)
    if completed_todo and completed_todo.completed:
        print(f"[OK] Service marked complete: {completed_todo.title}, Status: {completed_todo.completed}")
    else:
        print("[ERROR] Service failed to mark complete")
        return False

    incomplete_todo = service.mark_incomplete(service_todo.id)
    if incomplete_todo and not incomplete_todo.completed:
        print(f"[OK] Service marked incomplete: {incomplete_todo.title}, Status: {incomplete_todo.completed}")
    else:
        print("[ERROR] Service failed to mark incomplete")
        return False

    # Test deleting via service
    deleted_via_service = service.delete_todo(service_todo.id)
    if deleted_via_service:
        print("[OK] Service deleted todo successfully")
    else:
        print("[ERROR] Service failed to delete todo")
        return False

    print("\n[OK] All functionality tests passed!")
    return True

def run_manual_test():
    """Provide instructions for manual testing"""
    print("\nManual Testing Instructions:")
    print("1. Run: PYTHONPATH=. python src/todo_app/main.py")
    print("2. Try these commands:")
    print("   - help (to see available commands)")
    print("   - add 'Buy groceries' (to add a todo)")
    print("   - list (to view all todos)")
    print("   - update 1 'Buy weekly groceries' (to update a todo)")
    print("   - complete 1 (to mark a todo as complete)")
    print("   - incomplete 1 (to mark a todo as incomplete)")
    print("   - delete 1 (to delete a todo)")
    print("   - exit (to quit the application)")

if __name__ == "__main__":
    success = test_todo_app()
    run_manual_test()

    if success:
        print("\n[SUCCESS] All automated tests passed!")
    else:
        print("\n[FAILURE] Some tests failed!")
        sys.exit(1)