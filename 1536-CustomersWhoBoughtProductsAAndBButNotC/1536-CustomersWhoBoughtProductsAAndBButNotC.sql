-- Last updated: 6/25/2026, 9:10:48 AM
# Write your MySQL query statement below
with test as (
    select * ,
    case 
    when product_name='C' then 1
    when product_name='A' then 2
    when product_name='B' then 3
    else 0 end check1
    from Orders )
    

select distinct a.customer_id , a.customer_name from Customers a
left join Orders b
on a.customer_id=b.customer_id where a.customer_id  in  (
select customer_id from test group by customer_id having sum(check1)=5)
