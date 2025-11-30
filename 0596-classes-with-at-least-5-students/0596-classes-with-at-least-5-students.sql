# Write your MySQL query statement below
select class from Courses
GROUP BY class
Having COUNT(student)>=5
