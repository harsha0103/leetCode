-- Last updated: 6/25/2026, 9:13:13 AM
# Write your MySQL query statement below
select * from cinema where id%2 != 0 and description != 'boring'  order by rating   desc