-- Last updated: 6/25/2026, 9:15:53 AM
# Write your MySQL query statement belo
with cte as  (select salary, Dense_rank()over(order by salary desc) as rnk from Employee)

select  (select distinct salary  from cte where rnk=2) as  SecondHighestSalary


