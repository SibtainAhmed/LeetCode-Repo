# Write your MySQL query statement below
select
t1.machine_id, 
ROUND(avg(t1.timeStamp - t2.timestamp), 3) as processing_time 
from Activity as t1 join Activity as t2
using(machine_id, process_id)
where t2.activity_type = 'start' and t1.activity_type = 'end'
group by machine_id;
