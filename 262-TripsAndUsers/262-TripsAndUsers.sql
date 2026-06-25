-- Last updated: 6/25/2026, 9:14:48 AM
# Write your MySQL query statement below

with bannedUsers as (
    select users_id from Users where role='client' and banned='Yes'
),
bannedDrivers as(
    select users_id from Users where role='driver' and banned='Yes'
),
up_trips as (
    select client_id,driver_id, 
    case  when status= 'completed' then 0
        else 1 end as st
    ,request_at from Trips 
    where client_id not in (select * from bannedUsers) and 
    driver_id not in (select * from bannedDrivers ) 
)
select request_at as 'Day', round(sum(st)/count(st),2) as 'Cancellation Rate' from up_trips 
where request_at BETWEEN '2013-10-01' AND '2013-10-03'group by request_at 