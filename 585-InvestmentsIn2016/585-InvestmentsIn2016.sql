-- Last updated: 6/25/2026, 9:13:30 AM
# Write your MySQL query statement below
with unique_ll as (
    select pid  from Insurance group by lat,lon having count(*)<2
),
repeated_id as(
    select distinct tiv_2015  from Insurance group by tiv_2015 having count(tiv_2015)>1
)
select round(sum(tiv_2016),2) as tiv_2016 from Insurance where tiv_2015 in (select tiv_2015 from repeated_id ) and pid in (select pid from unique_ll)