-- Last updated: 6/25/2026, 9:10:23 AM
# Write your MySQL query statement below
select customer_id, count(*) as count_no_trans from Visits a left join Transactions b 
on a.visit_id=b.visit_id 
where b.visit_id is null
group by customer_id