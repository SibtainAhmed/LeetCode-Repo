# Write your MySQL query statement below
-- select name as results from Users 
-- where user_id in 
-- select user_id from MovieRating
-- group by user_id
-- having count(*)=
-- (select max(select count(*) from MovieRating group by user_id) as mx from Users)
-- order by name
-- limit 1

(select m1.name as results from Users as m1 join
(select user_id, count(rating) as freq from MovieRating
group by user_id) as m2
using(user_id) 
order by freq desc, name
limit 1)

union all
(select m1.title as results from Movies as m1 join
(select movie_id, avg(rating) as freq from MovieRating
where created_at between '2020-02-01' and '2020-02-29'
group by movie_id) as m2
using(movie_id) 
order by freq desc, title 
limit 1);