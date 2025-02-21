# Write your MySQL query statement below
select Visits.customer_id , COUNT(Visits.visit_id) AS count_no_trans
FROM Visits LEFT JOIN Transactions ON Visits.visit_id =  Transactions.visit_id
WHERE Transactions.visit_id IS Null
GROUP BY Visits.customer_id