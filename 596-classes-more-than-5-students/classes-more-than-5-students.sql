# Write your MySQL query statement below
select c.class from Courses as c group by c.class having count(1)>4;