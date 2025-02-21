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

def open_tasks_list():
    """Opens the tasks list in read mode"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            try:
                tasks = json.load(f)
            except json.JSONDecodeError:
                tasks = []
            return tasks
    else:
        initialise_tasks_file()
        return []

def extract_task_description():
    """Gets description of task as provided by user"""
    if len(sys.argv) < 3:
        print("Error: Task description not provided.")
        print("Usage: python main.py add \"task description\"")
        sys.exit(1)
    
    description = " ".join(sys.argv[2:])
    return description

def main():
    open_tasks_list()

    if len(sys.argv) > 1 and sys.argv[1] == "add":
        task_description = extract_task_description()
        print("Task Description:", task_description)

if __name__ == "__main__":
    main()