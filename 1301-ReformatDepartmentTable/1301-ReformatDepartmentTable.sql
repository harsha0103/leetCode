-- Last updated: 6/25/2026, 9:11:19 AM
# Write your MySQL query statement below


select id, sum(case when `month`='Jan' then revenue else null End) as Jan_Revenue, 
            sum(case when `month`='Feb' then revenue else null End) as Feb_Revenue,
            sum(case when `month`='Mar' then revenue else null End) as Mar_Revenue,
            sum(case when `month`='Apr' then revenue else null End) as Apr_Revenue,
            sum(case when `month`='May' then revenue else null End) as May_Revenue,
            sum(case when `month`='Jun' then revenue else null End) as Jun_Revenue,
            sum(case when `month`='Jul' then revenue else null End) as Jul_Revenue,
           sum( case when `month`='Aug' then revenue else null End) as Aug_Revenue,
            sum(case when `month`='Sep' then revenue else null End) as Sep_Revenue,
            sum(case when `month`='Oct' then revenue else null End) as Oct_Revenue,
            sum(case when `month`='Nov' then revenue else null End) as Nov_Revenue,
            sum(case when `month`='Dec' then revenue else null End) as Dec_Revenue
            from Department group by id 