Feature: Search by none existing priority
    @nonePriority
    Scenario: Filter task by a none existing priority 
        Given the to-do list
        | DESCRIPTION                   | DATE       | STATUS        | PRIORITY |
        | Buy Book: Animal Farm         | 23-07-2023 | COMPLETED     | LOW      |
        | Buy groceries                 | 01-08-2023 | NOT_COMPLETED | MEDIUM   |
        | Software Engineerig homework  | 31-07-2023 | IN_PROGRESS   | HIGH     |
        | Clean the bathroom            | 08-08-2023 | NOT_COMPLETED | HIGH     |
        When the user search by a none existing priority "ULTRA HIGH"
        Then show no task on the to-do list
        And the to-do list is
        | DESCRIPTION                   | DATE       | STATUS        | PRIORITY |
        |                               |            |               |          |

