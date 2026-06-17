# Write your MySQL query statement below
SELECT W.name AS Employee FROM Employee W
JOIN Employee M
WHERE M.id = W.managerId
AND W.salary >= M.salary