-- Last updated: 6/25/2026, 9:11:45 AM
# Write your MySQL query statement below
with cte as (
    select product_id, `year` as fy,  quantity, price, Dense_rank() over(partition by product_id 
    order by `year` ) as rnk from Sales
)

select product_id,fy as first_year ,  quantity, price from cte where rnk=1