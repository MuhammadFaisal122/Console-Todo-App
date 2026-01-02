# Quickstart Guide: Console Todo App

## Prerequisites
- Python 3.13 or higher
- UV package manager (for dependency management)

## Setup
1. Clone or create the project directory
2. Navigate to the project root
3. Install dependencies (if any): `uv sync` (or `pip install -r requirements.txt`)

## Running the Application
1. Execute: `python src/todo_app/main.py`
2. The application will start in REPL mode with a prompt
3. Type `help` or `?` to see available commands

## Basic Usage

### Adding a Todo
```
> add "Buy groceries"
✓ Todo added with ID: 1
```

### Viewing Todos
```
> view
1 ○ Buy groceries
2 ○ Complete project
```
- ○ indicates incomplete
- ✓ indicates complete

### Updating a Todo
```
> update 1 "Buy weekly groceries"
✓ Todo updated successfully
```

### Marking Complete
```
> complete 2
✓ Todo marked as complete
```

### Deleting a Todo
```
> delete 1
✓ Todo deleted successfully
```

## Available Commands
- `add "description"` - Add a new todo
- `view` - List all todos
- `update <id> "new description"` - Update a todo
- `delete <id>` - Delete a todo
- `complete <id>` - Mark as complete
- `incomplete <id>` - Mark as incomplete
- `help` - Show help
- `exit` - Exit the application

## Error Handling
- Invalid commands will show an error message
- Non-existent IDs will return appropriate error messages
- Empty descriptions will be rejected