# Write your MySQL query statement below
-- select a.user_id, count(b.user_id) as followers_count 
-- from Followers as a join Followers as b on b.user_id = a.follower_id
-- group by a.user_id order by a.user_id;

select user_id, count(*) as followers_count from Followers group by user_id 
order by user_id