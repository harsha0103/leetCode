-- Last updated: 6/25/2026, 9:15:45 AM
# Write your MySQL query statement below
-- join the same table 

select a.name as Employee from (
select a.*, b.salary as man_salary from Employee a left join Employee b on a.managerId = b.id
) a  where a.salary > a.man_salary