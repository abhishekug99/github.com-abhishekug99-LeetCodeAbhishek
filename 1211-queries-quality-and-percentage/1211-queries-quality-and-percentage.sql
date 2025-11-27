# Write your MySQL query statement below
select query_name,
ROUND(AVG(rating*1.0/position),2) AS quality,
ROUND(100.0*SUM(CASE WHEN rating<3 then 1 else 0 end)/COUNT(*), 2) AS poor_query_percentage
FROM Queries
Group BY query_name