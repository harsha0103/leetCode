-- Last updated: 6/25/2026, 9:13:33 AM
# Write your MySQL query statement below

select dept_name,count(student_id) as student_number from department left join student on student.dept_id = department.dept_id
group by 1
order by student_number desc
