-- Last updated: 6/25/2026, 9:11:22 AM
# Write your MySQL query statement below
with temp as (select count(*) from Delivery where order_date = customer_pref_delivery_date)

select round((select * from temp)/count(*)*100,2) as immediate_percentage  from Delivery
