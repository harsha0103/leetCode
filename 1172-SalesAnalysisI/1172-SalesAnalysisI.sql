-- Last updated: 6/25/2026, 9:11:36 AM
#solution one
#select seller_id from Sales group by seller_id having sum(price) =
#(select sum(price) as test  from Sales group by seller_id order by test desc limit 1 ) 

#solution 2 

with ntable as (select sum(price) as test  from Sales group by seller_id order by test desc limit 1) 

select seller_id from  Sales group by seller_id having  sum(price)= (select test from ntable) 