-- Last updated: 6/25/2026, 9:11:43 AM
# Write your MySQL query statement below
select project_id, round(avg(experience_years),2) as average_years  from Project a
inner join Employee b on a.employee_id=b.employee_id group by project_id