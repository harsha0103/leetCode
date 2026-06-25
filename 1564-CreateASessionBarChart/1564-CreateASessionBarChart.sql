-- Last updated: 6/25/2026, 9:10:42 AM
# Write your MySQL query statement below

select c.bin as BIN, sum(c.tot) as TOTAL from (
(select "[0-5>" as bin, CASE WHEN (duration/60) < 5 THEN 1 else 0 end as tot from Sessions)
union all 
(select "[5-10>" as bin, CASE WHEN (5 <= (duration/60) and (duration/60) <10) THEN  1 else 0 end as tot from Sessions)
union all 
(select "[10-15>" as bin, CASE WHEN (10 <= (duration/60) and (duration/60) <15) THEN  1 else 0 end as tot from Sessions)
union all 
(select "15 or more" as bin, CASE WHEN (15 <= (duration/60)) THEN  1 else 0 end as tot from Sessions)) c group by bin 


