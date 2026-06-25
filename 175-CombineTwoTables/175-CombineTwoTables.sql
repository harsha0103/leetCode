-- Last updated: 6/25/2026, 9:15:51 AM
# Write your MySQL query statement belo

select firstName, lastName, city,  state from Person a 
    left join Address b on a.personId=b.personId