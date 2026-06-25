-- Last updated: 6/25/2026, 9:11:01 AM
# Write your MySQL query statement below

select ad_id , coalesce( round((sum(clicked)/(sum(clicked)+sum(Viewed)))*100,2),0) as ctr  from (
select ad_id, case  when action = 'Clicked' then sum(1) else 0 end as clicked, case  when action = 'Viewed' then sum(1) else 0 end as Viewed
from Ads group by action,ad_id ) c group by ad_id order by ctr desc,ad_id