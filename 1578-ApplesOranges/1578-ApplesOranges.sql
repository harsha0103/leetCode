-- Last updated: 6/25/2026, 9:10:39 AM
# Write your MySQL query statement below

select * from (select a.sale_date,a.sold_num-b.sold_num as diff from Sales a
left join Sales b on 
a.fruit= 'apples' and b.fruit='oranges' and a.sale_date= b.sale_date) c where diff is not null
