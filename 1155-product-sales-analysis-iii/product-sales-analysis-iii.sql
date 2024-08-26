# Write your MySQL query statement below
select s1.product_id, s1.year as first_year, s1.quantity as quantity
, s1.price from
Sales as s1 join 
(
select sale_id, product_id, min(year) as fYear
from Sales group by product_id 
-- having year = min(year)
)
as s2
on s1.product_id = s2.product_id and fYear = s1.year
-- group by s1.product_id
-- where product_id IN (select product_id as p from Product)