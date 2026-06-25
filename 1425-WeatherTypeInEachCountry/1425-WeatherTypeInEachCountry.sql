-- Last updated: 6/25/2026, 9:11:09 AM
# Write your MySQL query statement below
select country_name , case when avg(weather_state)<= 15 then 'Cold'
                            when (avg(weather_state)>15 and  avg(weather_state)<25) then  'Warm'
                            else 'Hot' end as weather_type from Countries 
left join Weather on Countries.country_id =Weather.country_id where day like '2019-11%' group by country_name  