-- Last updated: 6/25/2026, 9:10:41 AM
# Write your MySQL query statement below
with test as (select b.left_operand,b.operator, b.right_operand , a.value value1,c.value as value2 from Variables a left join Expressions b
on a.name=b.left_operand left join Variables c on c.name=b.right_operand
             and b.left_operand is not null)

select left_operand,operator, right_operand,
case 
when (operator = '=') and (value1=value2 )  then  'true'
when (operator = '>') and (value1 > value2 )  then  'true'
when (operator = '<') and (value1 < value2 )  then  'true'
else
'false'
end as value 
from test where left_operand is not null