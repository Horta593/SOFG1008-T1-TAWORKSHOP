from datetime import datetime
from src.utils.enums import Status, Priority

class Task():
    def __init__(self, description, due_date ,priority="LOW"):
        self.description = description
        self.due_date = datetime.strptime(due_date, "%d-%m-%Y").date().strftime("%d-%m-%Y")
        self.status = Status.NOT_COMPLETED
        self.priority = Priority[priority]

    def __str__(self):
        return f"Task:\nDescription:{self.description} Priority: {self.priority.name} Status: {self.status.name} Due to: {self.due_date} "