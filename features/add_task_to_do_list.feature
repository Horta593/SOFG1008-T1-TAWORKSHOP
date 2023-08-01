Feature: Add a task to the to-do list
    @addTask
    Scenario: Adding a task
        Given the to-do list is empty
        When the user adds a task
        | TASK                          | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm         | 23/08/2023 | Not Completed | Low      | 
        Then the to-do list should contain 
        And the task add is
        | TASK                          | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm         | 23/08/2023 | Not Completed | Low      |
