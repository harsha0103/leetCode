-- Last updated: 6/25/2026, 9:10:37 AM
with cte as (
  select id, login_date,
         lead(login_date, 4, null) OVER (partition by id ORDER BY login_date) as next
  from (select distinct * from Logins) c
)
select id, name from Accounts
where id in (select id from cte where next is not null and DATEDIFF(next, login_date) = 4)
order by id