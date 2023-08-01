# Add a new task to the to-do list.
# • List all the tasks in the to-do list.
# • Mark a task as completed.
# • Clear the entire to-do list.

# Get todo list tasks by date range
# Get todo list by priority (high, medium, low)
# Get todo list by status (completed, not completed)

from datetime import datetime
from enum import Enum


class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class Status(Enum):
    COMPLETED = 1
    NOT_COMPLETED = 2
    IN_PROGRESS = 3


class Task():
    def __init__(self, description, priority="LOW"):
        self.description = description
        self.date = datetime.now()
        self.status = Status.NOT_COMPLETED
        self.priority = Priority[priority]

    def __str__(self):
        return f"{self.description} priority: {self.priority.name} status: {self.status.name} created: {self.date} "


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

    def get_tasks_by_date_range(self, start_date, end_date):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        for task in self.tasks:
            if task.date >= start_date and task.date <= end_date:
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


def main():
    print("Welcome to the Todo List App of T1!")
    todo_list = TodoList()
    user_quit = False

    while not user_quit:
        print()
        print("What would you like to do?")
        print("1. Add a new task")
        print("2. List all the tasks")
        print("3. Mark a task as completed")
        print("4. Clear the entire to-do list")
        print("5. Get to-dos by priority")
        print("6. Get to-dos by status")
        print("7. Get to-dos by creation date")
        print("8. Quit")

        user_input = input("Enter your choice: ")

        if user_input == "1":
            description = input("Enter the task description: ")
            priority = input("Enter the priority (HIGH, LOW, MEDIUM): ")
            created_task = Task(description, priority)
            todo_list.add_task(created_task)
        elif user_input == "2":
            todo_list.list_tasks()
        elif user_input == "3":
            description = input("Enter the task description: ")
            todo_list.mark_task_completed(description)
        elif user_input == "4":
            todo_list.clear_tasks()
        elif user_input == "5":
            priority = input("Enter the priority (HIGH, LOW, MEDIUM): ")
            todo_list.get_tasks_by_priority(priority)
        elif user_input == "6":
            status = input("Enter the status (COMPLETED, NOT_COMPLETED, IN_PROGRESS): ")
            todo_list.get_tasks_by_status(status)
        elif user_input == "7":
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            todo_list.get_tasks_by_date_range(start_date, end_date)
        elif user_input == "8":
            user_quit = True
        else:
            print("Invalid input")

    print("Thank you for using the Todo List App!")


if __name__ == "__main__":
    main()