-- Last updated: 6/25/2026, 9:13:36 AM
# Write your MySQL query statement below


select a.name from (
select a.id, a.name, count(*) as count from Candidate a join Vote b on a.id = b.candidateId group by 1, 2 
    ) a order by count desc limit 1