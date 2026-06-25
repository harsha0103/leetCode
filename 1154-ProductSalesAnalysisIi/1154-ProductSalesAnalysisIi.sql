-- Last updated: 6/25/2026, 9:11:44 AM
# Write your MySQL query statement below
select a.product_id , b.total_quantity  from product a
inner join (select product_id, sum(quantity) as total_quantity from Sales group by product_id) b
on a.product_id=b.product_id