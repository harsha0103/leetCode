-- Last updated: 6/25/2026, 9:10:58 AM
# Write your MySQL query statement below
with users1 as (
    select b.name, count(a.user_id) over (partition by a.user_id)  cou from MovieRating  a 
    left join Users b on a.user_id =b.user_id
),
mov as(
    select created_at,title,rating from MovieRating a 
    left join Movies b on a.movie_id=b.movie_id 
),
avg_mov as (select title ,avg(rating) as cou from mov  where  created_at >='2020-02-01' and created_at < '2020-03-01' group by title)


(select distinct name as results from users1 where (select max(cou) from users1)=cou order by name limit 1)
union  all
(select title as results from avg_mov where (select max(cou) from avg_mov)=cou order by title limit 1)