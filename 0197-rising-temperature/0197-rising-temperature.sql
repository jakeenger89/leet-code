SELECT 
    d2.id
FROM
    Weather d1
JOIN 
    Weather d2 ON DATEDIFF(d2.recordDate, d1.recordDate) = 1
WHERE
    d2.temperature > d1.temperature;