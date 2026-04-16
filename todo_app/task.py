# task.py

from datetime import datetime

class Task:
    def __init__(self, task_id, title, done=False, created_at=None):
        self.task_id = task_id
        self.title = title
        self.done = done
        # If loading from file, use saved date. If new task, use now.
        self.created_at = created_at or datetime.now().strftime("%d-%m-%Y %I:%M %p")

    def mark_complete(self):
        self.done = True

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "done": self.done,
            "created_at": self.created_at   # ← new
        }

    @staticmethod
    def from_dict(data):
        return Task(
            task_id=data["id"],
            title=data["title"],
            done=data["done"],
            created_at=data.get("created_at")  # ← .get() handles old saves gracefully
        )

    def __str__(self):
        status = "✅" if self.done else "⬜"
        return f"{self.task_id}. {status} {self.title}  🕐 {self.created_at}"