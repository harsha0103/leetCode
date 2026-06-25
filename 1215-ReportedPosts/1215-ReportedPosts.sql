-- Last updated: 6/25/2026, 9:11:29 AM
# Write your MySQL query statement below
select extra as report_reason , count(distinct post_id) as report_count   from Actions where action_date ='2019-07-04' and action ='report'  group by extra order by extra