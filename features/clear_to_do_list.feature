Feature: Clear the entire to do list.
    @clearTodo
        Scenario: Delete all tasks of to do list.
            Given a set of todo list
            | TASK                 | DATE       | STATUS      | PRIORITY|
            | Clean the car        | 31/07/2023 | IN_PROGRESS | MEDIUM  |
            | Buy the bottle water | 30/07/2023 | IN_PROGRESS | LOW     |
            When the user click on "Delete" icon
            Then the todo list should be empty.
            | TASK                 | DATE       | STATUS       | PRIORITY |
