-- Last updated: 6/25/2026, 9:09:59 AM
# Write your MySQL query statement below
with cte as (select account_id, income, case when income <20000 then 'Low Salary'
                        when income <=50000  and income >=20000 then 'Average Salary'
                        else 'High Salary' end as category
 from Accounts) ,
 cte1 as (select category,count(category)   as accounts_count from cte  group by category
             union  All
            select 'Low Salary' as category,0 as accounts_count
             union  All
            select 'Average Salary' as category,0 as accounts_count
             union  All
            select 'High Salary' as category,0 as accounts_count
            )

select category,sum(accounts_count)  as accounts_count from cte1 group by category
order by  
case category when "Low Salary" then 1
when "Average Salary" then 2 
when "High Salary" then 3
end

