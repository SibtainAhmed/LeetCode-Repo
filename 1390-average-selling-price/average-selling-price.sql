# Write your MySQL query statement below
select 
P.product_id, ifnull(ROUND(sum(price*units)/sum(units),2),0) as average_price
from Prices as P left join UnitsSold as U 
on P.product_id=U.product_id 
and purchase_date BETWEEN start_date AND end_date
-- P.start_date<= U.purchase_date and U.purchase_date <= P.end_date
group by P.product_id;