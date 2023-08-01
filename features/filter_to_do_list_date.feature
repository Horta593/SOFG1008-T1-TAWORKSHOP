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

