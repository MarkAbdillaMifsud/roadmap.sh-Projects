import os
import json
import sys
from datetime import datetime

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

def update_task_description(task_id, new_description):
    """
    Update an existing task description by task ID

    Args:
        task_id: int
        new_description: string
    """
    tasks = load_tasks_list()

    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            task_found = True
            break
    
    if not task_found:
        print(f"Task with ID {task_id} not found.")
    else:
        save_tasks_list(tasks)
        print(f"Task with ID {task_id} updated successfully.")

def update_task_status(task_id):
    """Update an existing task status from to do to in-progress, by task ID
    
    Args:
        task_id: int
    """

    tasks = load_tasks_list()

    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "todo":
                task["status"] = "in-progress"
                task["updatedAt"] = datetime.now().isoformat()
                task_found = True
                break
            else:
                print("Task is already in progress")
                task_found = True
                break
    
    if not task_found:
        print(f"Task with ID {task_id} not found.")
    else:
        save_tasks_list(tasks)
        print(f"Task with ID {task_id} updated successfully.")

def delete_task(task_id):
    """
    Delete an existing task from the JSON by task ID

    Args:
        task_id: int
    """
    tasks = load_tasks_list()

    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            task_found = True
            break
    
    if not task_found:
        print(f"Task with ID {task_id} not found.")
    else:
        save_tasks_list(tasks)
        print(f"Task with ID {task_id} deleted successfully.")

def main():
    load_tasks_list()

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "add":
            task_description = extract_task_description()
            add_task(task_description)
        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: Task ID and new description are required.")
                print("Usage: python main.py update <task_id> \"new description\"")
                sys.exit(1)
            
            try:
                task_id = int(sys.argv[2])
            except ValueError:
                print("Error: Task ID should be an integer")
                sys.exit(1)
            
            new_description = " ".join(sys.argv[3:])
            update_task_description(task_id, new_description)
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Task ID is required.")
                print("Usage: python main.py update <task_id>")
                sys.exit(1)
            
            try:
                task_id = int(sys.argv[2])
            except ValueError:
                print("Error: Task ID should be an integer")
                sys.exit(1)
            
            delete_task(task_id)
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Error: Task ID is required.")
                print("Usage: python main.py update <task_id>")
                sys.exit(1)
            
            try:
                task_id = int(sys.argv[2])
            except ValueError:
                print("Error: Task ID should be an integer")
                sys.exit(1)
            update_task_status(task_id)
        else:
            print("Command not recognized. Available commands: add, update, delete, mark-in-progress")
    else:
        print("Usage: python main.py <command> [arguments]")

if __name__ == "__main__":
    main()