-- Last updated: 6/25/2026, 9:10:44 AM
# Write your MySQL query statement below
select b.id,b.year,
COALESCE(npv,0) AS npv from NPV a
right join Queries  b on a.id=b.id
and b.year   =a.year order by id,year


