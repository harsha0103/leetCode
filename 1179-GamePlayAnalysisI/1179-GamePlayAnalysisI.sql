-- Last updated: 6/25/2026, 9:11:34 AM
# Write your MySQL query statement below


select player_id, min(event_date) as first_login from Activity group by player_id