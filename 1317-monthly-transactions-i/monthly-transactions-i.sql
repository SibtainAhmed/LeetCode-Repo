# Write your MySQL query statement below
select month, country, count(*) as trans_count, sum(approvedStatus) as approved_count, sum(amount) as trans_total_amount, sum(case when approvedStatus=1 then amount else 0 end) as approved_total_amount
from Transactions as t1 join 
(SELECT id,

       DATE_FORMAT(trans_date, '%Y-%m') AS month,
 Case when state = 'approved' then 1 else 0 end as approvedStatus
 

FROM Transactions) as t2 on t1.id=t2.id
group by t2.month, t1.country;