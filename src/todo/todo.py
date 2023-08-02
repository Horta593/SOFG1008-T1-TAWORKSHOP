from datetime import datetime
from utils.enums import Status

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
        by_date_range = []
        start_date = datetime.strptime(start_date, "%d-%m-%Y").date().strftime("%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y").date().strftime("%d-%m-%Y")
        for task in self.tasks:
            if task.due_date >= start_date and task.due_date <= end_date:
                print(task)
                by_date_range.append(task)
        return by_date_range

    def get_tasks_by_priority(self, priority):
        by_priority = []
        for task in self.tasks:
            if task.priority.name == priority:
                print(task)
                by_priority.append(task)
        return by_priority

    def get_tasks_by_status(self, status):
        by_status = []
        for task in self.tasks:
            if task.status.name == status:
                print(task)
                by_status.append(task)
        return by_status

    def get_tasks_by_description(self, description):
        for task in self.tasks:
            if task.status.description == description:
                return task
        return None

    def delete_task(self, description):
        for i,task in enumerate(self.tasks):
            if task.status.description == description:
                del self.tasks[i]
                return True
        return False

    def clear_tasks(self):
        self.tasks = []



