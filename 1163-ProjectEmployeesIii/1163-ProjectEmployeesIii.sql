-- Last updated: 6/25/2026, 9:11:40 AM
# Write your MySQL query statement below


with test1 as (select a.project_id, b.employee_id,Dense_Rank () over(partition by a.project_id order by b.experience_years desc) as rank1 from Project a
left join Employee b on a.employee_id= b.employee_id)

select project_id,employee_id from test1 where rank1=1