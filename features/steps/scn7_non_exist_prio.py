from behave import *
from src.main import * 

#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

# Step 1: Given the to-do list
@given('the to-do list') 
def step_impl(context):
# Set the to-do list 
    global to_do_list
    to_do_list = TodoList()

    for row in context.table:
        to_do_list.add_task(row["DESCRIPTION"],row["PRIORITY"])

    context.todolist = to_do_list

# Step 2: When the user search by a none existing priority "ULTRA HIGH"
@when('the user search by a none existing priority "{task}"') 
def step_impl(context, task):
    # Add the task to the to-do list
    found_todoList = TodoList()

    for t in context.todolist:
        if t.priority == task:
            tsk = Task(t.description, t.priority)
            found_todoList.add_task(tsk)

    context.found_todoList = found_todoList

# Step 3: Then show no task on the to-do list
@then('show no task on the to-do list') 
def step_impl(context):
    # Show no task of the to do list 
    context.found_todoList
    assert context.found_todoList == 0, f'Exist a none existing priority!'
