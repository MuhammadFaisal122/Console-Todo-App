"""
Todo Model

This module defines the Todo data model for the console todo application.
"""
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Todo:
    """
    Represents a todo item with id, title, and completion status.
    """
    id: int
    title: str
    completed: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        """Set created_at timestamp if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()

    def mark_complete(self):
        """Mark the todo as complete."""
        self.completed = True
        self.updated_at = datetime.now()

    def mark_incomplete(self):
        """Mark the todo as incomplete."""
        self.completed = False
        self.updated_at = datetime.now()

    def update_title(self, new_title: str):
        """Update the todo title."""
        self.title = new_title
        self.updated_at = datetime.now()