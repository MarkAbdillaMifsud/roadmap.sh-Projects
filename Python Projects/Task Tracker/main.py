import os
import json
import sys

TASKS_FILE = "tasks.json"

def initialise_tasks_file():
    """Checks if file exists and creates one if not found"""
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)
        print(f"Created placeholder {TASKS_FILE} with an empty task list.")
    else:
        print(f"{TASKS_FILE} already exists.")

def main():
    initialise_tasks_file()

    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return
    
    command = sys.argv[1]

    if command == "add":
        print("Add command invoked.")
    elif command == "update":
        print("Update command invoked.")
    elif command == "delete":
        print("Delete command invoked.")
    elif command == "list":
        print("List command invoked.")
    else:
        print("Unknown command. Available commands: add, update, delete, list")

if __name__ == "__main__":
    main()