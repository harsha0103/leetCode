-- Last updated: 6/25/2026, 9:13:29 AM
# Write your MySQL query statement below
select customer_number  from Orders group by customer_number order by count(customer_number) desc limit 1