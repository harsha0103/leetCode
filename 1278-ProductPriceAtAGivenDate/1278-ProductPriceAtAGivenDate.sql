-- Last updated: 6/25/2026, 9:11:23 AM
# Write your MySQL query statement below


with first_occ as( select product_id,new_price as price, rank() over( partition by product_id 
                order by change_date desc )rnk from Products where  change_date<='2019-08-16'  ),

 second_occ as ( select product_id,10 as price from Products where product_id not in
             (select product_id from first_occ) )


select product_id, price from  first_occ where rnk=1
union
select product_id, price  from second_occ 