-- Last updated: 6/25/2026, 9:15:41 AM
# Write your MySQL query statement below
with cte as (
    select departmentId, salary, name, Dense_rank () over( partition by departmentId order by salary desc) rnk from Employee
)

select b.name as Department,  a.name as Employee, salary from cte a 
inner join Department b on a.departmentId=b.id and a.rnk=1

