-- Last updated: 6/25/2026, 9:11:37 AM
# Write your MySQL query statement below
-- with cte as (select player_id,device_id, rank () over(partition by player_id order by event_date ) as rnk from Activity)

-- select player_id, device_id from cte where rnk=1


# make it faster 

select player_id, device_id from Activity where (player_id, event_date) in (
    select player_id, min(event_date) as event_date from activity group by player_id
)