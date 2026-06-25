-- Last updated: 6/25/2026, 9:09:54 AM
# Write your MySQL query statement below


with cust_0 as (select distinct customer_id, sum(order_type)  over(partition by customer_id )=
                count(order_type) over(partition by customer_id )  as bool from orders)


select * from orders a where a.customer_id IN (SELECT customer_id FROM cust_0 WHERE bool=1)
   OR (a.customer_id IN (SELECT customer_id FROM cust_0 WHERE  bool=0) AND a.order_type = 0)