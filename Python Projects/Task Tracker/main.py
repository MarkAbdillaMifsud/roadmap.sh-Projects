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

def load_tasks_list():
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

def save_tasks_list(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def extract_task_description():
    """Gets description of task as provided by user"""
    if len(sys.argv) < 3:
        print("Error: Task description not provided.")
        print("Usage: python main.py add \"task description\"")
        sys.exit(1)
    
    description = " ".join(sys.argv[2:])
    return description

def generate_task_id(tasks):
    """Generate a unique task ID on existing tasks
    
    param: tasks - list: A list of task dictionaries
    return: int: A unique task ID
    """

    if not tasks:
        return 1 # Since no tasks found, create task ID 1
    
    max_id = max(task["id"] for task in tasks)
    return max_id + 1

def add_task(description):

    tasks = load_tasks_list()

    new_id = generate_task_id(tasks)

    from datetime import datetime
    now = datetime.now().isoformat()
    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(task)
    save_tasks_list(tasks)

    print(f"Task added successfully (ID: {new_id})")

def main():
    load_tasks_list()

    if len(sys.argv) > 1 and sys.argv[1] == "add":
        task_description = extract_task_description()
        add_task(task_description)

if __name__ == "__main__":
    main()