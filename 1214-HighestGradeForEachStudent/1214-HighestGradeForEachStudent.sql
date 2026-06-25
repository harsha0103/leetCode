-- Last updated: 6/25/2026, 9:11:30 AM
# Write your MySQL query statement below

with test as (
select  student_id ,course_id,grade  ,Row_Number() over(partition by student_id order by grade desc,course_id) as grades  from Enrollments)

select student_id ,course_id,grade from test where grades = 1
