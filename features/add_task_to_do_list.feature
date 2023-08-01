Feature: Add a task to the to-do list
    @addTask
    Scenario: Adding a task
        Given the to-do list is empty
        When the user adds
        | DESCRIPTION                   | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm         | 31/07/2023 | NOT_COMPLETED | LOW      | 
        Then the to-do list should contain "Buy Book: Animal Farm,LOW"
        And the task add is
        | DESCRIPTION                   | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm         | 31/07/2023 | NOT_COMPLETED | LOW      |
