class TaskManagerLogic:
    def __init__(self, tasks):
        self.tasks = tasks

    def add_task(self, description, category, priority, due_date):

        for task in self.tasks:
            if(task["description"] == description and
               task["category"] == category and
               task["priority"] == priority and
               task["due_date"] == due_date):
                return False # If there are dupplicates, the task won't be added

            
        #If there are no dupplicates, add the task : 

        task = {
            "description": description,
            "category": category,
            "priority": priority,
            "due_date": due_date,
            "completed" : False
        }

        self.tasks.append(task)
        return True

    def delete_task(self,index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            if not self.tasks[index]["completed"]:
                self.tasks[index]["completed"] = True
                return True
            else:
                return False
            
    def get_tasks(self):
        return self.tasks
    
