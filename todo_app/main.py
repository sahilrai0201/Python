# main.py

from task_manager import TaskManager

def show_menu():
    print("\n==== 📝 To-Do List ====")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Search tasks")        # ← new
    print("6. Exit")                # ← was 5
    print("=======================")

def main():
    manager = TaskManager()
    print("👋 Welcome to your To-Do List App!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            manager.view_tasks()

        elif choice == "2":
            title = input("Enter task title: ").strip()
            if title:
                manager.add_task(title)
            else:
                print("⚠️  Task title cannot be empty!")

        elif choice == "3":
            manager.view_tasks()
            try:
                task_id = int(input("Enter task ID to mark complete: ").strip())
                manager.complete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid number!")

        elif choice == "4":
            manager.view_tasks()
            try:
                task_id = int(input("Enter task ID to delete: ").strip())
                manager.delete_task(task_id)
            except ValueError:
                print("❌ Please enter a valid number!")

        elif choice == "5":                                        # ← new
            keyword = input("Enter keyword to search: ").strip()
            if keyword:
                manager.search_tasks(keyword)
            else:
                print("⚠️  Please enter a keyword!")

        elif choice == "6":                                        # ← was 5
            print("👋 Goodbye! Stay productive!")
            break

        else:
            print("⚠️  Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()