import sys
import json

def add_task(task):
    """Add a task to tasks.json."""
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    
    tasks.append({"task": task, "done": False})
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks():
    """List all tasks from tasks.json."""
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        if not tasks:
            print("No tasks found.")
            return
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else " "
            print(f"{i}. [{status}] {task['task']}")
    except FileNotFoundError:
        print("No tasks found.")

def main():
    """Handle CLI arguments."""
    if len(sys.argv) < 2:
        print("Usage: python tracker.py [add|list] [task]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) == 3:
        add_task(sys.argv[2])
        print(f"Added task: {sys.argv[2]}")
    elif command == "list":
        list_tasks()
    else:
        print("Invalid command. Use: python tracker.py [add|list] [task]")
        sys.exit(1)

if __name__ == "__main__":
    main()
