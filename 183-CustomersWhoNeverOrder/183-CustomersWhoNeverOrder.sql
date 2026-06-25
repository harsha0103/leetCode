-- Last updated: 6/25/2026, 9:15:43 AM
# Write your MySQL query statement below
select name as Customers from Customers  where id not in (select customerId from Orders)