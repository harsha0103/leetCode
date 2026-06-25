-- Last updated: 6/25/2026, 9:11:02 AM
# Write your MySQL query statement below

with cte as (
    select visited_on, sum(amount) as amount  from Customer group by visited_on
),
final as (select visited_on,
        avg(amount) over( order by visited_on ROws between 6 preceding  and current row) as average_amount ,
        sum(amount) over( order by visited_on rows between 6 preceding and current row) as amount,
        row_number() over(order by visited_on) as r
        from cte)

select visited_on,amount,round(average_amount,2) average_amount from final where r>=7