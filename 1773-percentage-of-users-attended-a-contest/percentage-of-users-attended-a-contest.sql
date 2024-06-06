# Write your MySQL query statement below
select R.contest_id, 
round(count(U.user_id)/(select count(user_id) from Users)*100, 2) as percentage
from Register as R join Users as U using(user_id)
group by R.contest_id
order by percentage desc, R.contest_id;