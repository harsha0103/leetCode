-- Last updated: 6/25/2026, 9:10:18 AM
# Write your MySQL query statement below
select machine_id, 

ROUND(
    
    (SUM(CASE when activity_type = 'end' then timestamp END)-SUM(CASE when activity_type = 'start' then timestamp END))/count(distinct process_id)
    
    ,3) processing_time

from Activity 

group by 1


