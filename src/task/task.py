from datetime import datetime
from utils.enums import Status, Priority

class Task():
    def __init__(self, description, due_date ,priority="LOW"):
        self.description = description
        self.due_date = datetime.strptime(due_date, "%d-%m-%Y").date().strftime("%d-%m-%Y")
        self.status = Status.NOT_COMPLETED
        self.priority = Priority[priority]

    def __str__(self):
        return f"Task:\nDescription:{self.description} Priority: {self.priority.name} Status: {self.status.name} Due to: {self.due_date} "

    def __hash__(self):
        return hash((self.description, self.due_date, self.priority, self.status))

    def __eq__(self, other):
        if not isinstance(other, Task):
            return NotImplemented
        return self.description == other.description and self.due_date == other.due_date and self.priority == other.priority and self.status == other.status
