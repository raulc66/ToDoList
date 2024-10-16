import json
import os

def save_tasks(tasks, filename = 'tasks.json'):
    with open(filename, 'w') as f:
        json.dump(tasks, f)
    print("Tasks saved.")

def load_tasks(filename = 'tasks.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f :
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Error: Invalid JSON format in file.")
                return []
            
    else:
        print("No tasks file found. Starting with an empty list.")
        return []    
