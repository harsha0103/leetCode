-- Last updated: 6/25/2026, 9:10:05 AM
# Write your MySQL query statement below
with cte as (
    select  order_id,max(quantity) over (partition by  order_id) maximum, 
            avg(quantity) over (partition by  order_id) average from OrdersDetails 
 )
select  distinct order_id from cte where maximum > (select max(average) from cte) 