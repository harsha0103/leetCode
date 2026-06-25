-- Last updated: 6/25/2026, 9:13:21 AM
# Write your MySQL query statement below
with temp as (select seat_id, free ,lead(free,1)OVER (ORDER BY seat_id) as l,lag(free,1)OVER (ORDER BY seat_id)  as la from cinema)

select seat_id from temp where  free=1 and (l=1 or la=1) order by seat_id