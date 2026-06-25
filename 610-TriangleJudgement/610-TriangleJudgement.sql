-- Last updated: 6/25/2026, 9:13:19 AM
# Write your MySQL query statement below
select *,case when((x+y>z and x<=z and y<=z) or (x+z>y and x<=y and y>=z) or (z+y>x and x>=z and y<=x)) then 'Yes' else 'No' end as triangle  from triangle