-- Last updated: 6/25/2026, 9:10:21 AM
# Write your MySQL query statement below
/*with available_drivers as (select ride_id, user_id, SUBSTRING_INDEX(requested_at, '-', 1) as year, SUBSTRING_INDEX(SUBSTRING_INDEX(requested_at, '-', 2), '-', -1) as month, SUBSTRING_INDEX(requested_at, '-', -1) as day from Rides)

, accepted_rides as (select available_drivers.ride_id, AcceptedRides.driver_id, available_drivers.month, available_drivers.year from AcceptedRides inner join available_drivers on AcceptedRides.ride_id = available_drivers.ride_id)

select month, (select count(distinct driver_id) from AcceptedRides where year = 2020)/(select count(distinct))

*/


with recursive months as (
select      1 as month
union all
select      month+1
from        months
where       month <12),

available_drivers as (
select      months.month, ifnull(max(t1.active_driver) over (order by month),0) as active_driver
from        months
left join   
(select     month(join_date) as month, count(driver_id) over (order by join_date rows unbounded preceding) as active_driver
from        drivers
where       year(join_date) <= 2020) t1
on          t1.month = months.month
),

working_drivers as (
select      month(requested_at) as month, count(distinct driver_id) as working_driver
from        Rides R
join        AcceptedRides A on R.ride_id = A.ride_id
where       year(requested_at) = 2020
group by    1)

#select * from months


select      months.month, ifnull(round(working_driver/active_driver*100,2),0) as working_percentage
from        months
left join   available_drivers on available_drivers.month = months.month
left join   working_drivers on working_drivers.month = months.month
group by    1
