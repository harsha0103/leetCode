-- Last updated: 6/25/2026, 9:11:06 AM
# Write your MySQL query statement below

select employee_id, d.team_size from employee a
left join 
(select team_id ,count(team_id) as team_size from employee group by  team_id) d 
on a.team_id=d.team_id