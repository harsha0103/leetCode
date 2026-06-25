-- Last updated: 6/25/2026, 9:13:17 AM
# Write your MySQL query statement below
with temp as (select a.name,c.name as color from salesperson a 
left join orders b on a.sales_id=b.sales_id
left join company c on b.com_id=c.com_id  )



select distinct name from salesperson where name not in (select distinct name from temp where color='RED')