# task_manager.py

from task import Task
from storage import save_tasks, load_tasks

class TaskManager:
    def __init__(self):
        self.tasks = self._load()

    def _load(self):
        raw = load_tasks()
        return [Task.from_dict(data) for data in raw]

    def _save(self):
        save_tasks([task.to_dict() for task in self.tasks])

    def _generate_id(self):
        if not self.tasks:
            return 1
        return max(task.task_id for task in self.tasks) + 1  # ← fixed ID logic

    def add_task(self, title):
        task = Task(task_id=self._generate_id(), title=title)
        self.tasks.append(task)
        self._save()
        print(f"✅ Task added: '{title}'")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks yet!")
            return

        print("\n📋 Your Tasks:")
        print("-" * 40)
        for task in self.tasks:
            print(task)
        print("-" * 40)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                if task.done:
                    print(f"⚠️  Task '{task.title}' is already done!")
                else:
                    task.mark_complete()
                    self._save()
                    print(f"🎉 Task '{task.title}' marked as complete!")
                return
        print(f"❌ No task found with ID {task_id}")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                self._save()
                print(f"🗑️  Task '{task.title}' deleted!")
                return
        print(f"❌ No task found with ID {task_id}")

    def search_tasks(self, keyword):                          # ← new method
        keyword = keyword.lower()
        results = [task for task in self.tasks if keyword in task.title.lower()]

        if not results:
            print(f"🔍 No tasks found matching '{keyword}'")
            return

        print(f"\n🔍 Results for '{keyword}':")
        print("-" * 40)
        for task in results:
            print(task)
        print("-" * 40)