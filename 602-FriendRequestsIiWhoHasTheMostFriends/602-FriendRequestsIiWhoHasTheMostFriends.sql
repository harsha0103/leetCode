-- Last updated: 6/25/2026, 9:13:23 AM
# Write your MySQL query statement below
with temo as (
select  accepter_id,requester_id from request_accepted 
union 
select requester_id as accepter_id, accepter_id as requester_id  from request_accepted)


select requester_id as id,count(requester_id) as num from ( select distinct accepter_id,requester_id from temo) c group by id order by num desc limit 1