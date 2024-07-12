-- Write your PostgreSQL query statement below
select t.tweet_id from Tweets as t where length(t.content)>15;