-- Last updated: 6/25/2026, 9:11:31 AM
# Write your MySQL query statement below

with cte as (select   player_id, datediff(event_date,lag(event_date,1) over(partition by player_id order by event_date)) as diff,
            rank() over(partition by player_id order by event_date ) as rnk from Activity)



select round((select count(distinct player_id ) from cte where diff =1 and rnk=2)/(select count(distinct player_id ) from Activity),2) as fraction