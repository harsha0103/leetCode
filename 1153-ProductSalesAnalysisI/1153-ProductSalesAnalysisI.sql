-- Last updated: 6/25/2026, 9:11:47 AM
# Write your MySQL query statement below
select product_name, year, price from Sales a inner join Product b on  a.product_id=b.product_id