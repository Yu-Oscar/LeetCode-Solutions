# Write your MySQL query statement below

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    select o.sales_id from Company c
    join Orders o
    on c.com_id = o.com_id
    where c.name = "RED"
)
