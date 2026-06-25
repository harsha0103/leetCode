-- Last updated: 6/25/2026, 9:15:46 AM
# Write your MySQL query statement below

with cte as (select num, lead(num,2) over( order by id)l2, lead(num,1) over( order by id)l1 from Logs)


select DISTINCT num as ConsecutiveNums from cte where num=l1 and num=l2