# Write your MySQL query statement below
select t1.customer_id from (select customer_id, 
product_key from Customer group by customer_id, product_key) as t1
group by t1.customer_id
having count(t1.product_key) = (select count(*) from Product)