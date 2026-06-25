-- Last updated: 6/25/2026, 9:09:46 AM
# Write your MySQL query statement below

with orderd_table as (
    select *, rank() over(partition by gender order by user_id) as rnk from Genders 
)
select user_id,gender from orderd_table order by rnk, 
 CASE gender
    WHEN 'Female' THEN 1
    WHEN 'other' THEN 2
    ELSE 3
  END