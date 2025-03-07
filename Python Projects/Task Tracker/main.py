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

def get_description(start_index=2):
    """Gets description of task as provided by user"""
    if len(sys.argv) < start_index + 1:
        print("Error: Task description not provided.")
        sys.exit(1)
    return " ".join(sys.argv[start_index:])

def get_task_id():
    """Gets task id as provided by user"""
    if len(sys.argv) < 3:
        print("Error: Task ID is required.")
        print("Usage: python main.py <command> <task_id> [additional arguments]")
        sys.exit(1)
    try:
        return int(sys.argv[2])
    except ValueError:
        print("Error: Task ID should be an integer.")
        sys.exit(1)

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
    """
    Add new task based on user's description

    Args:
        description: string
    """
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

def update_task_status(task_id, command):
    """Update an existing task status from to do to in-progress, by task ID
    
    Args:
        task_id: int
    """

    tasks = load_tasks_list()

    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            if command == "mark-in-progress":
                task["status"] = "in-progress"
                task["updatedAt"] = datetime.now().isoformat()
                task_found = True
                break
            elif command == "mark-to-do":
                task["status"] = "todo"
                task["updatedAt"] = datetime.now().isoformat()
                task_found = True
                break
            elif command == "mark-done":
                task["status"] = "done"
                task["updatedAt"] = datetime.now().isoformat()
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

def filter_tasks(status):
    """Filter tasks depending on their completion status

    Args:
        status: string
    
    Return:
        dict with filtered tasks
    """
    tasks = load_tasks_list()

    filtered_tasks = [task for task in tasks if task.get("status", "").lower() == status.lower()]
    if not filtered_tasks:
        print(f"No tasks found with status {status}")
    else:
        for task in filtered_tasks:
            print(task)       

def print_usage():
    """Prints instructions on usage"""
    print("Usage: python main.py <command> [arguments]")
    print("Available commands:")
    print("  add <task description>")
    print("  update <task_id> \"new description\"")
    print("  delete <task_id>")
    print("  mark-to-do <task_id>")
    print("  mark-in-progress <task_id>")
    print("  mark-done <task_id>")
    print("  filter <status>   (status can be: todo, in-progress, done)")

def process_add():
    description = get_description(start_index=2)
    add_task(description)

def process_update():
    if len(sys.argv) < 4:
        print("Error: Task ID and new description are required.")
        print_usage()
        sys.exit(1)
    task_id = get_task_id()
    new_description = get_description(start_index=3)
    update_task_description(task_id, new_description)

def process_delete():
    task_id = get_task_id()
    delete_task(task_id)

def process_status(command):
    task_id = get_task_id()
    update_task_status(task_id, command)

def process_filter(status):
    filter_tasks(status)

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit()
    
    command = sys.argv[1]

    command_dispatch = {
        "add": process_add,
        "update": process_update,
        "delete": process_delete,
        "mark-to-do": lambda: process_status("mark-to-do"),
        "mark-in-progress": lambda: process_status("mark-in-progress"),
        "mark-done": lambda: process_status("mark-done"),
        "filter": lambda: process_filter(sys.argv[2] if len(sys.argv) >= 3 else print("Error: Status is required for filter."))
    }

    action = command_dispatch.get(command)
    if action:
        action()
    else:
        print("Command not recognised")
        print_usage()

if __name__ == "__main__":
    main()