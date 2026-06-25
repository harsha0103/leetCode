-- Last updated: 6/25/2026, 9:13:09 AM
# Write your MySQL query statement below

update Salary set sex = case when sex = 'm' then 'f' when sex = 'f' then 'm' end
      
