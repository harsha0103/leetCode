-- Last updated: 6/25/2026, 9:15:35 AM
# Write your MySQL query statement below
with cte as (select id, temperature- lag(temperature,1) over(order by recordDate ) as res, 
            datediff(recordDate,lag(recordDate,1) over(order by recordDate )) d from Weather )
select id from cte where res>0 and d=1