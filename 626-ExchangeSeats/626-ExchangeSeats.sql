-- Last updated: 6/25/2026, 9:13:10 AM
select a.id, 
       case when  a.lead_num is null and (a.id % 2) != 0 then a.student 
            when (a.id % 2) != 0 then a.lead_num
            when (a.id % 2) = 0 then a.lag_num
             end as student
from
(
select id, 
       student,
       lag (student) over (order by id asc) as lag_num,
       lead (student) over (order by id asc) as lead_num
       from Seat
    ) a
