# Write your MySQL query statement below
SELECT w.id
from Weather w
Join Weather w1
ON DATEDIFF(w.recordDate, w1.recordDate) = 1
WHERE w.temperature > w1.temperature;
