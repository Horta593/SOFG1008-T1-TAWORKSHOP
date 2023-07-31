#language: en 

Feature: Mark a task as completed.

    @taskCompleted
    Scenario: Change status of task as completed.
        Given a set of todo list
        | TASK                 | DATE       | STATUS      | PRIORITY|
        | Clean the car        | 31/07/2023 | In Progress | Medium  |
        | Buy the bottle water | 30/07/2023 | In Progress | Low     |
        Given the user click on status of task
        When the user select "Completed" Status
        Then the status of task change to "Completed" and updated it.
        | TASK                 | DATE       | STATUS       | PRIORITY |
        | Clean the car        | 31/07/2023 | Completed    | Medium   |
        | Buy the bottle water | 30/07/2023 | In Progress  | Low      |

Feature: Clear the entire to do list.
    @clearTodo
        Scenario: Delete all tasks of to do list.
            Given a set of todo list
            | TASK                 | DATE       | STATUS      | PRIORITY|
            | Clean the car        | 31/07/2023 | In Progress | Medium  |
            | Buy the bottle water | 30/07/2023 | In Progress | Low     |
            When the user click on "Delete" icon
            Then the todo list should be empty.
            | TASK                 | DATE       | STATUS       | PRIORITY |


Feature: Change status of the task.
    @changeStatus
        Scenario: Change status of task.
            Given a set of todo list
            | TASK                 | DATE       | STATUS      | PRIORITY|
            | Clean the car        | 31/07/2023 | In Progress | Medium  |
            | Buy the bottle water | 30/07/2023 | In Progress | Low     |
            Given the user click on status of task
            When the user select "No Completed" Status
            Then the status of task change to "Completed" and updated it.
            | TASK                 | DATE       | STATUS          | PRIORITY |
            | Clean the car        | 31/07/2023 | No Completed    | Medium   |
            | Buy the bottle water | 30/07/2023 | In Progress     | Low      |


Feature: Delete task from to do list.
    @deleteTask
        Scenario: Remove task of to do list.
            Given a set of todo list
            | TASK                 | DATE       | STATUS      | PRIORITY|
            | Clean the car        | 31/07/2023 | In Progress | Medium  |
            | Buy the bottle water | 30/07/2023 | In Progress | Low     |
            When the user click on "Delete" icon on "Clean the car" task
            Then the task "Clean the car" should not be appear on todo list.
            | TASK                 | DATE       | STATUS       | PRIORITY |
            | Buy the bottle water | 30/07/2023 | In Progress  | Low      |


Feature: Add a task to the to-do list
    @addTask
    Scenario: Adding a task
        Given the To-Do list empty
        | TASK                          | DATE       | STATUS        | PRIORITY |
        |                               |            |               |          |
        When the user adds a task "Buy Book: Animal Farm"
        Then the to-do list should contain "Buy Book: Animal Farm" with the corresponding date "23/08/2023" and the status "Not Completed" and priority "low"
        And the task add is
        | TASK                          | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm         | 23/08/2023 | Not Completed | Low      |


Feature: List all tasks in the to-do list
    @listAllTask
    Scenario: List all task on the to-do list
        Given the To-Do list
        | TASK                          | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm         | 23/07/2023 | Completed     | Low      |
        | Buy groceries                 | 01/08/2023 | Not Completed | Medium   |
        | Software Engineerig homework  | 31/07/2023 | In Progress   | High     |
        | Clean the bathroom            | 08/08/2023 | Not Completed | High     |
        When the user list all tasks
        Then show all the to-do list 
        And all the to-do list is
        | TASK                          | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm         | 23/07/2023 | Completed     | Low      |
        | Buy groceries                 | 01/08/2023 | Not Completed | Medium   |
        | Software Engineerig homework  | 31/07/2023 | In Progress   | High     |
        | Clean the bathroom            | 08/08/2023 | Not Completed | High     |


Feature: Search by a none existing date
    @noneDate
    Scenario: Filter task by a none existing date
        Given the To-Do list
        | TASK                          | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm         | 23/07/2023 | Completed     | Low      |
        | Buy groceries                 | 01/08/2023 | Not Completed | Medium   |
        | Software Engineerig homework  | 31/07/2023 | In Progress   | High     |
        | Clean the bathroom            | 08/08/2023 | Not Completed | High     |
        When the user search by a none existing date "05/06/2020"
        Then show no task on the to-do list 
        And the to-do list is
        | TASK                          | DATE       | STATUS        | PRIORITY |
        |                               |            |               |          |


Feature: Give a none existing priority
    @nonePriority
    Scenario: Filter task by a none existing priority 
        Given the To-Do list
        | TASK                          | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm         | 23/07/2023 | Completed     | Low      |
        | Buy groceries                 | 01/08/2023 | Not Completed | Medium   |
        | Software Engineerig homework  | 31/07/2023 | In Progress   | High     |
        | Clean the bathroom            | 08/08/2023 | Not Completed | High     |
        When the user search by a none existing priority "Ultra High"
        Then show no task on the to-do list
        And the to-do list is
        | TASK                          | DATE       | STATUS        | PRIORITY |
        | 

