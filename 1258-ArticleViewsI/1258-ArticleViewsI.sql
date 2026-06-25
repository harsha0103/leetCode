-- Last updated: 6/25/2026, 9:11:26 AM
# Write your MySQL query statement below
select distinct author_id as id from Views where viewer_id = author_id  order by id asc 