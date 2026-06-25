-- Last updated: 6/25/2026, 9:10:35 AM
# Write your MySQL query statement belows
with cte as (
    select date_format (order_date,'%W') as d, item_category, sum(quantity) as quantity from Orders a
    right join Items b on a.item_id=b.item_id group by item_category,d )


select item_category as CATEGORY, 
        sum(case when d='Monday' then quantity else 0 end) as 'MONDAY',  
        sum(case when d='Tuesday' then quantity else 0 end) as 'TUESDAY',
        sum(case when d='Wednesday' then quantity else 0 end) as 'WEDNESDAY',
        sum(case when d='Thursday' then quantity else 0 end) as 'THURSDAY',
        sum(case when d='Friday' then quantity else 0 end) as 'FRIDAY',
        sum(case when d='Saturday' then quantity else 0 end) as 'SATURDAY',
        sum(case when d='Sunday' then quantity else 0 end) as 'SUNDAY'
from cte group by item_category order by category