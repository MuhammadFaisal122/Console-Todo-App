# CLI Interface Contract: Console Todo App

## Command Structure

The application provides a REPL (Read-Eval-Print Loop) interface with the following commands:

### Add Command
- **Syntax**: `add "todo description"`
- **Function**: Creates a new todo item with the given description
- **Response**: Confirmation message with assigned ID
- **Error cases**:
  - Empty description: Returns error message
  - Invalid syntax: Returns usage help

### View Command
- **Syntax**: `view` or `list`
- **Function**: Displays all todo items with their ID and completion status
- **Response**: Formatted list of all todos
- **Error cases**: None

### Update Command
- **Syntax**: `update <id> "new description"`
- **Function**: Updates the description of an existing todo item
- **Response**: Confirmation message
- **Error cases**:
  - Invalid ID: Returns error message
  - Non-existent ID: Returns error message
  - Empty description: Returns error message

### Delete Command
- **Syntax**: `delete <id>`
- **Function**: Removes a todo item by ID
- **Response**: Confirmation message
- **Error cases**:
  - Invalid ID: Returns error message
  - Non-existent ID: Returns error message

### Complete Command
- **Syntax**: `complete <id>`
- **Function**: Marks a todo item as complete
- **Response**: Confirmation message
- **Error cases**:
  - Invalid ID: Returns error message
  - Non-existent ID: Returns error message

### Incomplete Command
- **Syntax**: `incomplete <id>`
- **Function**: Marks a todo item as incomplete
- **Response**: Confirmation message
- **Error cases**:
  - Invalid ID: Returns error message
  - Non-existent ID: Returns error message

### Help Command
- **Syntax**: `help` or `?`
- **Function**: Displays available commands and usage
- **Response**: Help text with command syntax
- **Error cases**: None

### Exit Command
- **Syntax**: `exit` or `quit`
- **Function**: Exits the application
- **Response**: None
- **Error cases**: None

## Input Format
- Commands are case-sensitive
- Text arguments should be enclosed in quotes if they contain spaces
- IDs are positive integers

## Output Format
- Success messages: "✓ [operation] successful"
- Error messages: "✗ [error description]"
- Todo list format: "[ID] [status] Title" (e.g., "1 ✓ Buy groceries" or "2 ○ Complete project")