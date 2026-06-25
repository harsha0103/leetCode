-- Last updated: 6/25/2026, 9:11:32 AM
# Write your MySQL query statement below
select player_id, event_date, sum(games_played) over(partition by player_id order by event_date ) as games_played_so_far from Activity