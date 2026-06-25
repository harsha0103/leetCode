-- Last updated: 6/25/2026, 9:15:44 AM
# Write your MySQL query statement below
select email from (select email, count(email) c from Person group by email having c>1) a