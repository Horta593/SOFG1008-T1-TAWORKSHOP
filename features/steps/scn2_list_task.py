from behave import *

# Condiciones antes de empezar cualquier STEP


def before_scenario(context, scenario):
    context = {}

# Step 1: Given the to-do list
@given('the to-do list')
def step_impl(context):
    # Set the to-do list 
    global to_do_list
    to_do_list = [
        {"task": "Buy Book: Animal Farm",
         "date": "23/07/2023",
         "status": "Completed",
         "priority": "Low"
        },
        {"task": "Buy groceries",
         "date": "01/08/2023",
         "status": "Not Completed",
         "priority": "Medium"
        },
        {"task": "Software Engineerig homework",
         "date": "31/07/2023",
         "status": "In Progress",
         "priority": "High"
        },
        {"task": "Clean the bathroom",
         "date": "08/08/2023",
         "status": "Not Completed",
         "priority": "High"
        },
    ]
# Step 2: When the user adds a task "Buy Book: Animal Farm, 23/08/2023, Not Completed, low"
@when('the user list all {task}"')
def step_impl(context, task):
    # Add the task to the to-do list
    global to_do_list
    to_do_list.append(task)

# Step 3: Then the to-do list should contain "Buy Book: Animal Farm, 23/08/2023, Not Completed, low"
@then('show all the to-do list "{task}"')
def step_impl(context, task):
    # Check if the task is in the to-do list
    assert task in to_do_list, f'Task "{task}" not found in the to-dolist'
