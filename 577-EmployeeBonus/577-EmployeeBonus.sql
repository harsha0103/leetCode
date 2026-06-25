-- Last updated: 6/25/2026, 9:13:34 AM
# Write your MySQL query statement below
select name, bonus from Employee a
left join  Bonus b on a.empId =b.empId 
where bonus<1000 OR bonus is  null