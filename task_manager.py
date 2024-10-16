
tasks = []

def load_tasks(file_manager):
    global tasks
    tasks = file_manager.load_tasks()

def save_tasks(file_manager):
    file_manager.save_tasks(tasks)

def add_task(task_description):
    if task_description == "":
        raise ValueError("Task description cannot be empty.")

    if any(task['task'] == task_description for task in tasks):
        raise ValueError(f"Task '{task_description}' already exists.")  

    tasks.append({"task" : task_description, "completed" : False}) 

def delete_task(task_num):
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
    
    else:
        raise IndexError("Invalid task number.")

def complete_task(task_num):
    if 0 < task_num < len(tasks):
        tasks[task_num]["completed"] = True
    
    else: 
        raise IndexError("Invalid task number.")
    

def get_tasks():
    return tasks

