-- Last updated: 6/25/2026, 9:10:32 AM
# Write your MySQL query statement below
select sell_date,count(distinct product) as num_sold ,group_concat(distinct product order by product) as products  from Activities  group by sell_date