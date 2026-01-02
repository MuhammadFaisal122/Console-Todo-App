---
description: "Task list for Console Todo App implementation"
---

# Tasks: Console Todo App

**Input**: Design documents from `/specs/1-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Test tasks included as specified in the feature requirements

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/
- [X] T002 [P] Create src/todo_app/__init__.py
- [X] T003 [P] Create src/todo_app/models/__init__.py
- [X] T004 [P] Create src/todo_app/repositories/__init__.py
- [X] T005 [P] Create src/todo_app/services/__init__.py
- [X] T006 [P] Create src/todo_app/cli/__init__.py
- [X] T007 [P] Create src/todo_app/utils/__init__.py
- [X] T008 Create tests/__init__.py
- [X] T009 Create requirements.txt with Python 3.13+ specification
- [X] T010 Create README.md with project overview

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T011 Create Todo data model in src/todo_app/models/todo.py
- [X] T012 Create in-memory repository interface in src/todo_app/repositories/in_memory_repository.py
- [X] T013 Create todo service interface in src/todo_app/services/todo_service.py
- [X] T014 Create validation utilities in src/todo_app/utils/validators.py
- [X] T015 Create main application entry point in src/todo_app/main.py
- [X] T016 [P] Create CLI controller stub in src/todo_app/cli/cli_controller.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Users can add new todo items to their list

**Independent Test**: Can be fully tested by running the application, entering an "add" command with a todo description, and verifying the item appears in the todo list.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T017 [P] [US1] Unit test for Todo model in tests/test_todo_model.py
- [ ] T018 [P] [US1] Unit test for in-memory repository add functionality in tests/test_todo_repository.py
- [ ] T019 [P] [US1] Unit test for todo service add functionality in tests/test_todo_service.py

### Implementation for User Story 1

- [X] T020 [US1] Implement Todo model with id, title, completed attributes in src/todo_app/models/todo.py
- [X] T021 [US1] Implement add method in TodoRepository in src/todo_app/repositories/in_memory_repository.py
- [X] T022 [US1] Implement add_todo method in TodoService in src/todo_app/services/todo_service.py
- [X] T023 [US1] Implement CLI add command in src/todo_app/cli/cli_controller.py
- [X] T024 [US1] Connect add command to service layer in src/todo_app/main.py
- [X] T025 [US1] Add input validation for add command in src/todo_app/utils/validators.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todo Items (Priority: P1)

**Goal**: Users can view their list of todo items to see what tasks they need to complete

**Independent Test**: Can be fully tested by adding items to the list and then viewing the list to confirm all items are displayed correctly.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T026 [P] [US2] Unit test for repository get_all functionality in tests/test_todo_repository.py
- [ ] T027 [P] [US2] Unit test for service get_all functionality in tests/test_todo_service.py

### Implementation for User Story 2

- [X] T028 [US2] Implement get_all method in TodoRepository in src/todo_app/repositories/in_memory_repository.py
- [X] T029 [US2] Implement get_all_todos method in TodoService in src/todo_app/services/todo_service.py
- [X] T030 [US2] Implement CLI view command in src/todo_app/cli/cli_controller.py
- [X] T031 [US2] Connect view command to service layer in src/todo_app/main.py
- [X] T032 [US2] Add output formatting for todo list display in src/todo_app/utils/validators.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Todo Item (Priority: P2)

**Goal**: Users can update the description of existing todo items

**Independent Test**: Can be fully tested by adding an item, updating its description, and verifying the change is reflected in the list.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T033 [P] [US3] Unit test for repository update functionality in tests/test_todo_repository.py
- [X] T034 [P] [US3] Unit test for service update functionality in tests/test_todo_service.py

### Implementation for User Story 3

- [X] T035 [US3] Implement update method in TodoRepository in src/todo_app/repositories/in_memory_repository.py
- [X] T036 [US3] Implement update_todo method in TodoService in src/todo_app/services/todo_service.py
- [X] T037 [US3] Implement CLI update command in src/todo_app/cli/cli_controller.py
- [X] T038 [US3] Connect update command to service layer in src/todo_app/main.py
- [X] T039 [US3] Add validation for update command in src/todo_app/utils/validators.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Todo Item (Priority: P2)

**Goal**: Users can remove a todo item that is no longer needed

**Independent Test**: Can be fully tested by adding items, deleting one, and verifying it no longer appears in the list.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T040 [P] [US4] Unit test for repository delete functionality in tests/test_todo_repository.py
- [X] T041 [P] [US4] Unit test for service delete functionality in tests/test_todo_service.py

### Implementation for User Story 4

- [X] T042 [US4] Implement delete method in TodoRepository in src/todo_app/repositories/in_memory_repository.py
- [X] T043 [US4] Implement delete_todo method in TodoService in src/todo_app/services/todo_service.py
- [X] T044 [US4] Implement CLI delete command in src/todo_app/cli/cli_controller.py
- [X] T045 [US4] Connect delete command to service layer in src/todo_app/main.py
- [X] T046 [US4] Add validation for delete command in src/todo_app/utils/validators.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Todo Complete/Incomplete (Priority: P2)

**Goal**: Users can mark todo items as complete when finished, or mark as incomplete if needs more work

**Independent Test**: Can be fully tested by adding items, marking them complete/incomplete, and verifying the status updates.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T047 [P] [US5] Unit test for service mark complete/incomplete functionality in tests/test_todo_service.py

### Implementation for User Story 5

- [X] T048 [US5] Implement get_by_id method in TodoRepository in src/todo_app/repositories/in_memory_repository.py
- [X] T049 [US5] Implement mark_complete method in TodoService in src/todo_app/services/todo_service.py
- [X] T050 [US5] Implement mark_incomplete method in TodoService in src/todo_app/services/todo_service.py
- [X] T051 [US5] Implement CLI complete command in src/todo_app/cli/cli_controller.py
- [X] T052 [US5] Implement CLI incomplete command in src/todo_app/cli/cli_controller.py
- [X] T053 [US5] Connect complete/incomplete commands to service layer in src/todo_app/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T054 [P] Complete CLI controller with all commands in src/todo_app/cli/cli_controller.py
- [X] T055 [P] Add error handling and validation throughout application
- [X] T056 [P] Add help command implementation in src/todo_app/cli/cli_controller.py
- [X] T057 [P] Add exit command implementation in src/todo_app/main.py
- [X] T058 [P] Implement REPL loop in src/todo_app/main.py
- [X] T059 [P] Add comprehensive error messages per contract specification
- [X] T060 Run quickstart validation from specs/1-console-todo-app/quickstart.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints/CLI
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Todo model in tests/test_todo_model.py"
Task: "Unit test for in-memory repository add functionality in tests/test_todo_repository.py"
Task: "Unit test for todo service add functionality in tests/test_todo_service.py"

# Launch all implementation tasks for User Story 1 together:
Task: "Implement Todo model with id, title, completed attributes in src/todo_app/models/todo.py"
Task: "Implement add method in TodoRepository in src/todo_app/repositories/in_memory_repository.py"
Task: "Implement add_todo method in TodoService in src/todo_app/services/todo_service.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence