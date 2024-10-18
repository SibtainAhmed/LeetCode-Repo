# Write your MySQL query statement below
select product_id, new_price as price from Products
where (product_id, change_date) in
(select product_id, max(change_date) as math_date from Products
 where change_date <= '2019-08-16'
group by product_id order by change_date)
union
select product_id, 10 from Products
group by product_id
having min(change_date)>'2019-08-16';