#language: en

Feature: Mark a task as completed.
    @taskCompleted
    Scenario: Change status of task as completed.
        Given a set task of to-do list
        | DESCRIPTION          | DATE       | STATUS      | PRIORITY|
        | Clean the car        | 31-07-2023 | NOT_COMPLETED | MEDIUM  |
        | Buy the bottle water | 30-07-2023 | NOT_COMPLETED | LOW     |
        Given the user click on status of task required
        When the user select "Clean the car,NOT_COMPLETED" status of task
        Then the status of task should be change to "COMPLETED" and updated it.
        | DESCRIPTION          | DATE       | STATUS       | PRIORITY |
        | Clean the car        | 31-07-2023 | COMPLETED    | MEDIUM   |
        | Buy the bottle water | 30-07-2023 | NOT_COMPLETED  | LOW      |









