-- Last updated: 6/25/2026, 9:10:51 AM
# Write your MySQL query statement below
-- with cte as (
--     select stock_name, operation, sum(price)  as sm from stocks group by stock_name,operation
-- )

-- select a.stock_name, a.sm-b.sm as capital_gain_loss from cte a
-- left join  cte b  on a.stock_name=b.stock_name and a.operation != b.operation
-- where a.operation ='Sell'


select stock_name, 
        sum(case when operation ='Sell' then price else -price end) as capital_gain_loss 
        from Stocks
        group by stock_name