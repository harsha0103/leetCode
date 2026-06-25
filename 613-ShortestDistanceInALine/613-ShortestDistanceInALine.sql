-- Last updated: 6/25/2026, 9:13:16 AM
# Write your MySQL query statement below

select min(abs(a.x-b.x)) as shortest  from point a, point b  where a.x!= b.x


