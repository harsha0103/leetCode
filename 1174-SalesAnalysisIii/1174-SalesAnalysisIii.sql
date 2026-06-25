-- Last updated: 6/25/2026, 9:11:35 AM
# Write your MySQL query statement below
select distinct a.product_id,a.product_name  from Product a
left join Sales b on a.product_id= b.product_id
where '2019-01-01'< sale_date  and '2019-03-31'> sale_date and  a.product_id not in (select product_id  from Sales where  '2019-01-01'> sale_date  or '2019-03-31'< sale_date ) order by a.product_id