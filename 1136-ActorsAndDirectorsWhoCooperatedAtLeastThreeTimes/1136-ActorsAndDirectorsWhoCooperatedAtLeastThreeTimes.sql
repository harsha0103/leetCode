-- Last updated: 6/25/2026, 9:11:50 AM
# Write your MySQL query statement below
select actor_id,director_id  from (select actor_id, director_id  from ActorDirector) c group by actor_id,director_id  having count(*) >= 3