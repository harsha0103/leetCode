-- Last updated: 6/25/2026, 9:11:17 AM
# Write your MySQL query statement below
with con_mon as ( select id, country, state, amount, Date_format(trans_date,'%Y-%m') as mon from Transactions)

select  mon as `month`,country , count(amount) as trans_count ,
                    sum(case when state='approved' then 1 else 0 END) as  approved_count ,
                    sum(amount) as trans_total_amount,
                    sum(case when state='approved' then amount else 0 END) as  approved_total_amount
                    from con_mon group by mon,country

