-- Last updated: 6/25/2026, 9:13:26 AM
# Write your MySQL query statement below
select class    from Courses group by class having  count(class)>=5 