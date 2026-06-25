-- Last updated: 6/25/2026, 9:13:14 AM
# Write your MySQL query statement below
with dep_join as ( select a.amount,  DATE_FORMAT(a.pay_date, '%Y-%m') as pay_month,
            b.department_id  from Salary a  inner join Employee b on
            a.employee_id =b.employee_id  ),

avg_mon as ( select pay_month, avg(amount) as mon from dep_join group by pay_month),
avg_dep as ( select department_id,pay_month,avg(amount)  dep from dep_join group by department_id, pay_month ),

com_res as (select distinct  a.pay_month,a.department_id,b.mon,c.dep from dep_join a  
            left join avg_dep c on a.department_id=c.department_id and a.pay_month=c.pay_month
            left join avg_mon b on a.pay_month=b.pay_month order by a. pay_month )


select distinct pay_month, department_id, 
        case 
            when mon>dep then 'lower'
            when  mon<dep  then 'higher'
            else 'same'
        End  as  comparison  from com_res
