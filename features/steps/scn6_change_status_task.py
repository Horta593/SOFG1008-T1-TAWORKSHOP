from behave import *
from src.todo.todo import TodoList
from src.task.task import Task

# Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}

# Step 1: Given the to-do list
@given('a set of task from to-do list')
def step_impl(context):
    global to_do_list
    to_do_list  = TodoList()

    for row in context.table:
        tsk = Task(row["DESCRIPTION"],row["DATE"],row["PRIORITY"])
        to_do_list.add_task(tsk)

    context.to_do_list = to_do_list

@given('the user click on status of "{description}" task')
def step_given_user_clicks_on_status_of_task(context, description):
    context.task_description = description

@when('the user select "{status}" Status')
def step_impl(context,status):
    global to_do_list

    if status == 'COMPLETED':
        context.to_do_list.mark_task_completed(context.task_description)
    if status == 'IN_PROGRESS':
        context.to_do_list.mark_task_in_progress(context.task_description)
    if status == 'NOT_COMPLETED':
        context.to_do_list.mark_task_incomplete(context.task_description)

@then('the status of "{description}" task changes to "{status}" and updates it')
def step_impl(context,description, status):
    global to_do_list
    tasks = context.to_do_list.tasks
    for task in tasks:
        if task['TASK'] == description:
            assert task['STATUS'] == status, f'Status of task {description} did not change correctly'
            return
    assert False, f'Task {description} not found in the todo list'
