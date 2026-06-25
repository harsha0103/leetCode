-- Last updated: 6/25/2026, 9:15:47 AM
# Write your MySQL query statement below
select score, Dense_rank() over( order by score desc) as 'rank' from scores