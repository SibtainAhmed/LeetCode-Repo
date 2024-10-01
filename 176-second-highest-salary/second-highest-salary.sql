# Write your MySQL query statement below
select 
max(secondc) as SecondHighestSalary
from
(select distinct salary as secondc from Employee
-- group by salary
order by salary desc
limit 1
offset 1) as t1;