-- Last updated: 6/25/2026, 9:10:57 AM
# Write your MySQL query statement below
select distinct id, name  from Students where   department_id  not in  (select  id from departments)   