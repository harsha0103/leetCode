-- Last updated: 6/25/2026, 9:10:29 AM
# Write your MySQL query statement below
select * from Users where  regexp_like(mail,'^[a-zA-Z]+[a-zA-Z0-9\.\_\-]*@leetcode.com') order by User_ID