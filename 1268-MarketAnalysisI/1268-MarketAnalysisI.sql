-- Last updated: 6/25/2026, 9:11:24 AM
# Write your MySQL query statement below


with test as (select buyer_id,count(buyer_id) as  orders_in_2019 from Orders   where year(order_date) = '2019' group by buyer_id)

select a.user_id as buyer_id ,a.join_date,coalesce(b.orders_in_2019,0) as orders_in_2019 from Users a
left join test b on  a.user_id =b.buyer_id 