-- Last updated: 6/25/2026, 9:10:30 AM
# Write your MySQL query statement below
with tab as (select a.customer_id, a.name,Month(b.order_date) as month, sum(c.price*b.quantity) as t from Customers a
right join Orders b
on a.customer_id =b.customer_id 
left join Product c
on b.product_id=c.product_id   where b.order_date   like '2020-06-%'or b.order_date   like '2020-07-%' group by a.customer_id, Month(b.order_date) order by a.name)

select customer_id,name  from tab where t>=100  group by name having count(name)>1