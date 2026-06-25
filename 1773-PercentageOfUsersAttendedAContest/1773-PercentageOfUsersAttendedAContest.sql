-- Last updated: 6/25/2026, 9:10:22 AM
# Write your MySQL query statement below
select contest_id,ROUND((count(distinct user_id) * 100)/(select count(*) from Users),2) as percentage
from Register 
group by 1
order by percentage desc, contest_id