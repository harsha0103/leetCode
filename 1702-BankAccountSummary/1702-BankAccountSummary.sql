-- Last updated: 6/25/2026, 9:10:26 AM
# Write your MySQL query statement below
with tot_spent as (
    select paid_by, sum(amount) as amount  from  Transactions group by paid_by),

tot_received as(
    select paid_to, sum(amount) as amount from Transactions group by paid_to),

spent as (
    select a.user_id, a.user_name, a.credit-coalesce(b.amount,0)+ coalesce(c.amount,0) credit from Users a 
    left join tot_spent b on a.user_id=b.paid_by
    left join tot_received c on a.user_id=c.paid_to
)

select *, case when credit < 0 then 'Yes'
        else 'No' end as credit_limit_breached from spent 