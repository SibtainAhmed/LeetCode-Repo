# Write your MySQL query statement below
select Round(AVG(case when order_date = customer_pref_delivery_date then 1
else 0 END)*100, 2) AS immediate_percentage FROM Delivery 
where (customer_id, order_date) in
 (
    select customer_id, min(order_date) as order_date
    from Delivery
    group by customer_id
    
)