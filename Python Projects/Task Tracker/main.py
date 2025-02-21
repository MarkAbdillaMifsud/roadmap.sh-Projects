import os
import json

TASKS_FILE = "tasks.json"

def initialise_tasks_file():
    """Checks if file exists and creates one if not found"""
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)
        print(f"Created placeholder {TASKS_FILE} with an empty task list.")
    else:
        print(f"{TASKS_FILE} already exists.")

if __name__ == "__main__":
    initialise_tasks_file()