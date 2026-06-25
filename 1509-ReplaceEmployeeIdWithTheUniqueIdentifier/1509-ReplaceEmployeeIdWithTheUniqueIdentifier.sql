-- Last updated: 6/25/2026, 9:10:52 AM
# Write your MySQL query statement below
select unique_id, name from Employees a left join EmployeeUNI b on a.id = b.id