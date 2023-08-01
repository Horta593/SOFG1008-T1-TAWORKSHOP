from datetime import datetime
from src.utils.enums import Status

class TodoList():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = Status.COMPLETED
                break
    
    def mark_task_in_progress(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = Status.IN_PROGRESS
                break
    def mark_task_incomplete(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = Status.NOT_COMPLETED
                break
    
    def get_tasks_by_date_range(self, start_date, end_date):
        start_date = datetime.strptime(start_date, "%d-%m-%Y").date().strftime("%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y").date().strftime("%d-%m-%Y")
        for task in self.tasks:
            if task.due_date >= start_date and task.due_date <= end_date:
                print(task)

    def get_tasks_by_priority(self, priority):
        for task in self.tasks:
            if task.priority.name == priority:
                print(task)

    def get_tasks_by_status(self, status):
        for task in self.tasks:
            if task.status.name == status:
                print(task)

    def clear_tasks(self):
        self.tasks = []

    

