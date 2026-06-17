# Write your MySQL query statement below
select name as Customers from customers C 
left join orders O on C.id = O.customerId
where O.id is null