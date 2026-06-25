-- Last updated: 6/25/2026, 9:11:14 AM
# Write your MySQL query statement below
select distinct query_name,  round(sum(rating/position )/count(query_name),2) as quality,
                round( count(case when rating<3 then rating end) /count(query_name)*100,2) as poor_query_percentage  from Queries group by query_name 