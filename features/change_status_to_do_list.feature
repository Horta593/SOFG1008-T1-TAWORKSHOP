Feature: Change status of the task.
    @changeStatus
    Scenario: Change status of task.
        Given a set of todo list
        | DESCRIPTION          | DATE       | STATUS        | PRIORITY|
        | Clean the car        | 31-07-2023 | NOT_COMPLETED | MEDIUM  |
        | Buy the bottle water | 30-07-2023 | NOT_COMPLETED | LOW     |
        Given the user click on status of task
        When the user select "NOT_COMPLETED" Status
        Then the status of task change to "COMPLETED" and updated it.
        | DESCRIPTION          | DATE       | STATUS          | PRIORITY |
        | Clean the car        | 31-07-2023 | COMPLETED   | MEDIUM   |
        | Buy the bottle water | 30-07-2023 | IN_PROGRESS     | LOW      |

