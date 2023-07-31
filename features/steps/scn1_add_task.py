from behave import *

#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

# Step 1: Given the to-do list is empty
@given('the to-do list empty') 
def step_impl(context):
    # Set the to-do list as an empty list
    global to_do_list
    to_do_list = []
# Step 2: When the user adds a task "Buy Book: Animal Farm, 23/08/2023, Not Completed, low"
@when('the user adds a {task}"') 
def step_impl(context, task):
    # Add the task to the to-do list
    global to_do_list 
    to_do_list.append(task)

# Step 3: Then the to-do list should contain "Buy Book: Animal Farm, 23/08/2023, Not Completed, low"
@then('the to-do list should contain "{task}"') 
def step_impl(context, task):
    # Check if the task is in the to-do list
    assert task in to_do_list, f'Task "{task}" not found in the to-dolist'
