-- Last updated: 6/25/2026, 9:11:15 AM
# Write your MySQL query statement below

with weight as (
    select sum(weight) over (order by turn) as weight,turn from Queue 
)

select person_name  from Queue  where turn not in (select turn from weight where weight>1000) order by turn desc limit 1