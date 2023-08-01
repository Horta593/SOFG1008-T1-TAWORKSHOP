from behave import *
from src.main import * 

#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

# Step 1: Given the to-do list is empty
@given('the to-do list is empty') 
def step_impl(context):
# Set the to-do list as an empty list
    global to_do_list
    to_do_list = TodoList()
# Step 2: When the user adds 
@when('the user adds') 
def step_impl(context):
    # Add the task to the to-do list
    global to_do_list 
    for row in context.table:
        tsk = Task(row["DESCRIPTION"],row["PRIORITY"])
        to_do_list.add_task(tsk)
# Step 3: Then the to-do list should contain "Buy Book: Animal Farm,LOW"
@then('the to-do list should contain "{task}"') 
def step_impl(context, task):
# Check if the task is in the to-do list
    global to_do_list
    task_info = task.split(",")
    tsk = Task(task_info[0],task_info[1])
    for t in TodoList.tasks:
        if t.description == tsk.description:    
            assert True, f'Task is in the to-do list'
