# Write your MySQL query statement below
SELECT MAX(num) AS num
FROM MyNumbers
WHERE num IN (
    select num from MyNumbers 
    group by num
    Having count(*) = 1
    order by num DESC
)