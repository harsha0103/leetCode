-- Last updated: 6/25/2026, 9:15:34 AM
# Write your MySQL query statement below

with cte as (select id,email, rank ()over(partition by email order by id) as rnk from Person)


delete from Person a  where a.id in (select id from cte where rnk !=1)