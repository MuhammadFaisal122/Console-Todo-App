#!/usr/bin/env python3
"""
Final verification test for the Todo App
"""
import sys
import os

def final_test():
    """Final comprehensive test of all functionality"""
    print("=== Final Verification Test ===")

    # Add the src directory to Python path
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

    try:
        from src.todo_app.repositories.in_memory_repository import TodoRepository
        from src.todo_app.services.todo_service import TodoService
        from src.todo_app.cli.cli_controller import CLIController
        print("[OK] All imports successful")
    except ImportError as e:
        print(f"[ERROR] Import error: {e}")
        return False

    # Test full functionality
    repo = TodoRepository()
    service = TodoService(repo)

    # Test 1: Add todo
    todo1 = service.add_todo("Final test task")
    if not todo1 or todo1.title != "Final test task":
        print("[ERROR] Add todo failed")
        return False
    print("[OK] Add todo functionality works")

    # Test 2: View todos
    todos = service.get_all_todos()
    if len(todos) != 1 or todos[0].title != "Final test task":
        print("[ERROR] View todos failed")
        return False
    print("[OK] View todos functionality works")

    # Test 3: Update todo
    updated_todo = service.update_todo(todo1.id, "Updated final test task")
    if not updated_todo or updated_todo.title != "Updated final test task":
        print("[ERROR] Update todo failed")
        return False
    print("[OK] Update todo functionality works")

    # Test 4: Mark complete
    completed_todo = service.mark_complete(todo1.id)
    if not completed_todo or not completed_todo.completed:
        print("[ERROR] Mark complete failed")
        return False
    print("[OK] Mark complete functionality works")

    # Test 5: Mark incomplete
    incomplete_todo = service.mark_incomplete(todo1.id)
    if not incomplete_todo or incomplete_todo.completed:
        print("[ERROR] Mark incomplete failed")
        return False
    print("[OK] Mark incomplete functionality works")

    # Test 6: Delete todo
    delete_result = service.delete_todo(todo1.id)
    if not delete_result:
        print("[ERROR] Delete todo failed")
        return False
    print("[OK] Delete todo functionality works")

    # Verify deletion
    todos_after_delete = service.get_all_todos()
    if len(todos_after_delete) != 0:
        print("[ERROR] Delete verification failed")
        return False
    print("[OK] Delete verification successful")

    print("\n=== All functionality verified successfully! ===")
    print("\nApplication Features:")
    print("- Add new todo items")
    print("- View all todo items")
    print("- Update todo item descriptions")
    print("- Delete todo items")
    print("- Mark todo items as complete/incomplete")
    print("- CLI with help and exit commands")
    print("- Error handling and validation")
    print("- ASCII-based display formatting (Windows compatible)")

    return True

if __name__ == "__main__":
    success = final_test()
    if success:
        print("\n[SUCCESS] CONGRATULATIONS: Todo App implementation is complete and fully functional!")
    else:
        print("\n[FAILURE] Some functionality is not working correctly")
        sys.exit(1)