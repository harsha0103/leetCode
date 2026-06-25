-- Last updated: 6/25/2026, 9:10:54 AM
# Write your MySQL query statement below
with tes1 as (select activity, count(activity) as number from Friends group by activity)

select activity from (select activity,Dense_RANK() over(order by number) as test1,Dense_RANK() over(order by number desc) as test2 from tes1)c where  test1!=1 and test2!=1

#select activity from tes2 where test1 !=1 and test2 !=1 