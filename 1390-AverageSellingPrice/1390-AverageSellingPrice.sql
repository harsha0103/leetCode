-- Last updated: 6/25/2026, 9:11:18 AM
# Write your MySQL query statement below

select a.product_id, ROUND(sum(a.price* b.units)/sum(b.units),2) as average_price  from Prices a
left join UnitsSold b on a.product_id =b.product_id
and a.start_date <= b.purchase_date  and a.end_date >=b.purchase_date
group by a.product_id
