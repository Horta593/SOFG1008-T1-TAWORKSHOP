# from behave import *
# from src.todo.todo import TodoList
# from src.task.task import Task

# #Condiciones antes de empezar cualquier STEP
# def before_scenario(context, scenario):
# 	context = {}

# @given('a set of to-do list')
# def step_given_a_set_of_todo_list(context):
#     global to_do_list
#     to_do_list = TodoList()

#     for i,row in enumerate(context.table):
#         tsk = Task(row["DESCRIPTION"],row["DATE"],row["PRIORITY"])
#         context.to_do_list.add_task(tsk)



# @when('the user click on "Delete" icon')
# def step_when_user_clicks_on_delete(context):
#     context.todo_list.clear_tasks()

# @then('the todo list should be empty')
# def step_then_todo_list_should_be_empty(context):
#     assert len(context.todo_list.tasks) == 0, 'Todo list is not empty'
