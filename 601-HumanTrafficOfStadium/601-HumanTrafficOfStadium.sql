-- Last updated: 6/25/2026, 9:13:24 AM
# Write your MySQL query statement below
with cte as ( select *, (lead(people,1) over(order by visit_date) >=100) as le1,
                        (lead(people,2) over(order by visit_date) >=100) as le2,
                        (lag(people,1) over(order by visit_date) >=100) as la1,
                        (lag(people,2) over(order by visit_date)>=100) as la2 from Stadium)

select  DISTINCT id, visit_date, people  from cte where people>= 100 and ( (le1 and le2) or (la1 and la2) or (le1 and la1)) order by visit_date 