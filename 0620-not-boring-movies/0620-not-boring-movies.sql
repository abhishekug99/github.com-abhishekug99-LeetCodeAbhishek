# Write your MySQL query statement below

select * from Cinema
WHERE id%2=1 AND description != 'boring'
Order BY rating Desc