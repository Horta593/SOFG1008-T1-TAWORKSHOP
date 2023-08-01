from behave import *
from src.todo.todo import TodoList
from src.task.task import Task
# Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}

# Step 1: Given the to-do list
@given('the to-do list')
def step_impl(context):
    # Set the to-do list
    global to_do_list
    to_do_list  = TodoList()

    for row in context.table:
        to_do_list.add_task(row["DESCRIPTION"],row["PRIORITY"])

# Step 2: When the user list all tasks
@when('the user list all ')
def step_impl(context):
    # Add the task to the to-do list
    global to_do_list

# Step 3: Then show all the to-do list 
@then('show all the to-do list')
def step_impl(context):
    # Print all the to-do list
    to_do_list.list_tasks()
    