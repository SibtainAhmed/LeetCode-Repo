# Write your MySQL query statement below
-- select 
-- (
    select max(num) as num from (select num from MyNumbers group by num having count(*)=1) as table1
--  as num