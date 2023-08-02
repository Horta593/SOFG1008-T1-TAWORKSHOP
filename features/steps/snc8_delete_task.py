# from behave import *
# from src.todo.todo import TodoList
# from src.task.task import Task

# @given('a set of todo list')
# def step_given_a_set_of_todo_list(context):
#     context.todo_list = TodoList()
#     for row in context.table:
#         task = dict(row.items())
#         context.todo_list.add_task(task)

# @when('the user click on "Delete" icon on "{task_description}" task')
# def step_when_user_clicks_on_delete_for_task(context, task_description):
#     context.todo_list.delete_task(task_description)

# @then('the task "{task_description}" should not be appear on todo list')
# def step_then_task_should_not_be_in_todo_list(context, task_description):
#     assert context.todo_list.delete_task(task_description)==False, f'Task {task_description} is still in the todo list'
