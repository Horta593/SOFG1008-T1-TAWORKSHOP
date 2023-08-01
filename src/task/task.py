from datetime import datetime
from src.utils.enums import Status, Priority

class Task():
    def __init__(self, description, priority="LOW"):
        self.description = description
        self.date = datetime.now()
        self.status = Status.NOT_COMPLETED
        self.priority = Priority[priority]

    def __str__(self):
        return f"{self.description} priority: {self.priority.name} status: {self.status.name} created: {self.date} "