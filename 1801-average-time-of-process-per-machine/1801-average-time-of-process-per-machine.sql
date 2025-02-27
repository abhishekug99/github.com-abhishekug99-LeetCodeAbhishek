# Write your MySQL query statement below
SELECT 
    machine_id, 
    ROUND(AVG(end_time - start_time), 3) AS processing_time
FROM (
    SELECT 
        A1.machine_id, 
        A1.process_id, 
        A2.timestamp AS end_time, 
        A1.timestamp AS start_time
    FROM Activity A1
    JOIN Activity A2 
    ON A1.machine_id = A2.machine_id AND A1.process_id = A2.process_id
    WHERE A1.activity_type = 'start' 
    AND A2.activity_type = 'end'
) AS process_times
GROUP BY machine_id;

