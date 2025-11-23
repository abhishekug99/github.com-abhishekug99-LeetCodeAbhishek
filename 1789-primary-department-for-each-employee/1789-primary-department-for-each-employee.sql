# Write your MySQL query statement below
select DISTINCT employee_id, department_id
from Employee
Where primary_flag = 'Y'
    or employee_id IN(
        select employee_id
        from Employee
        Group BY employee_id
        Having COUNT(*) = 1
    )