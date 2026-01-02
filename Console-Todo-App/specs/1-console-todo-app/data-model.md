# Data Model: Console Todo App

## Entity: Todo Item

**Description**: Represents a task that needs to be completed

**Attributes**:
- `id`: Integer - Unique identifier for the todo item (auto-generated)
- `title`: String - The description/text of the todo item (required, non-empty)
- `completed`: Boolean - The completion status of the todo item (default: False)

**Validation Rules**:
- `id` must be unique within the repository
- `title` must not be empty or None
- `completed` must be a boolean value

**State Transitions**:
- Initial state: `completed = False`
- When marked complete: `completed = True`
- When marked incomplete: `completed = False`

**Operations**:
- Create: Initialize with title, id auto-generated, completed=False
- Read: Access all attributes
- Update: Modify title or completion status
- Delete: Remove from repository

## Repository Interface: TodoRepository

**Description**: In-memory storage for Todo items

**Methods**:
- `get_all() -> List[Todo]`: Returns all todo items
- `get_by_id(id: int) -> Optional[Todo]`: Returns todo with specified id or None
- `add(todo: Todo) -> Todo`: Adds a new todo and returns it with assigned id
- `update(todo: Todo) -> Optional[Todo]`: Updates existing todo, returns updated todo or None if not found
- `delete(id: int) -> bool`: Deletes todo by id, returns True if successful
- `clear() -> None`: Removes all todos (not currently used but available for future)

## Service Interface: TodoService

**Description**: Business logic layer for todo operations

**Methods**:
- `add_todo(title: str) -> Todo`: Creates and adds a new todo with the given title
- `get_all_todos() -> List[Todo]`: Returns all todos
- `get_todo_by_id(id: int) -> Optional[Todo]`: Returns todo by id or None
- `update_todo(id: int, title: str) -> Optional[Todo]`: Updates the title of an existing todo
- `delete_todo(id: int) -> bool`: Deletes a todo by id
- `mark_complete(id: int) -> Optional[Todo]`: Marks a todo as complete
- `mark_incomplete(id: int) -> Optional[Todo]`: Marks a todo as incomplete