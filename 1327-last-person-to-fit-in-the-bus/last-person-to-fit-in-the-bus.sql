# Write your MySQL query statement below
select 
-- first_value(person_name) over() as person_name, 
last_value(person_name) over() as person_name
from
(
    select person_name, 
 SUM(weight) OVER (ORDER BY turn) as succSum
from Queue
) as t1
where succSum <= 1000
limit 1;