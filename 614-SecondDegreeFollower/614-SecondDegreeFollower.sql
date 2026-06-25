-- Last updated: 6/25/2026, 9:13:15 AM
# Write your MySQL query statement below

with temp as (select followee , count( distinct follower) as num from follow  
where followee != follower   group by followee)

select followee as follower , num from temp where followee  in (select distinct follower   from follow ) order by followee