# Write your MySQL query statement below
select S.student_id, S.student_name, S2.subject_name, 
count(e.subject_name) as attended_exams
from Students as S cross join Subjects as S2
left join Examinations as e 
on S.student_id = e.student_id and S2.subject_name = e.subject_name
group by S.student_id, S2.subject_name
order by S.student_id, S2.subject_name;