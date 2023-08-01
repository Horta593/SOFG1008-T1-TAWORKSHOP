Feature: List all tasks in the to-do list
    @listAllTask
    Scenario: List all task on the to-do list
        Given the to-do list
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
