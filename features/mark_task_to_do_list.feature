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









