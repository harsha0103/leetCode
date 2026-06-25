-- Last updated: 6/25/2026, 9:13:25 AM
# Write your MySQL query statement below
#with temp as (select   distinct a.sender_id,a.send_to_id, b.accepter_id  from friend_request a left join request_accepted b on a.sender_id =b.requester_id and send_to_id=accepter_id)

#select ifnull(round(sum(case when accepter_id is null then 0 else 1 end)/count(sender_id),2),0.00) as accept_rate from temp


select

round(
ifNull(
(select count(distinct requester_id,accepter_id) as dis from request_accepted)
/
(select count(distinct sender_id,send_to_id) as dis from friend_request)
,0),2)

as accept_rate;