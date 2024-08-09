# Write your MySQL query statement below
-- select round(sum(consec_login)/count(*), 2) as fraction from
-- (select 
-- round(sum(case when temp.login_date+1 = a.event_date then 1
-- else 0 end)/count(distinct temp.player_id),2)
-- as fraction
--  from Activity as a join 
-- (select player_id, min(event_date) as login_date 
-- from Activity group by player_id) as temp 
-- using(player_id))
-- group by player_id
-- ) as FinalTable;

-- select round(sum(case when temp.min_date + 1 = a.event_date then 1 else 0 end)
-- /
-- count(distinct temp.player_id), 2) as fraction
-- from (select player_id, min(event_date) as min_date from activity group by player_id) as temp
-- join activity a
-- on temp.player_id = a.player_id

select round(count(a.player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity), 2) as fraction from Activity
as a join (select player_id, min(event_date) as first_login from Activity group by player_id) as temp
using(player_id) where DATE_SUB(a.event_date, INTERVAL 1 DAY) = temp.first_login; 

-- select 
-- count(select distinct player_id from Activity)
--     as cnt from Activity
