-- Last updated: 6/25/2026, 9:13:39 AM
# Write your MySQL query statement below


with cte as (select managerId from Employee group by managerId having count(managerId) >=5)

select  name from Employee where id in (select * from cte) 