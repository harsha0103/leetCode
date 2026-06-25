-- Last updated: 6/25/2026, 9:15:40 AM
# Write your MySQL query statement below


with cte as (
    select departmentId,name, salary, Dense_rank()over(partition by departmentId order by salary desc  ) as rnk from Employee order by departmentId
)


select a.name as department,b.name as Employee, b.salary  from cte b
inner join Department a on a.id= b.departmentId
where rnk<=3