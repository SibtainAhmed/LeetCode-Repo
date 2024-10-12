# Write your MySQL query statement below
select id, student 
from 
(select id-1 as id, student from Seat where id%2=0
union
select id+1 as id, student from Seat where id%2=1 
and id != (select count(*) from Seat)
union
select * from Seat where id%2=1 and id=(select count(*) from Seat)) as t1
order by id