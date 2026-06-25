-- Last updated: 6/25/2026, 9:11:00 AM
# Write your MySQL query statement below
select a.product_name,sum(b.unit) as unit from Products a
left join orders b on a.product_id= b.product_id    
where  b.order_date like '2020-02-%'  group by a.product_name  having unit >= 100
