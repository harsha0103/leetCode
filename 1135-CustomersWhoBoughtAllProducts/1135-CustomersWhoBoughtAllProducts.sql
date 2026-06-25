-- Last updated: 6/25/2026, 9:11:51 AM
# Write your MySQL query statement below
with cte as ( select c.customer_id, count(c.customer_id) as cou from (select distinct customer_id, product_key from Customer) c group by c.customer_id  ),
count_product as ( select count(*) as cou from Product) 


select customer_id from cte  where cou=(select cou from count_product )
