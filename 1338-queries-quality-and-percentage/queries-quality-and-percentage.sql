# Write your MySQL query statement below
select q.query_name , round(sum(indQuality)/count(indQuality), 2) as quality,
round((sum(qualityPerc)/count(qualityPerc))*100, 2) as poor_query_percentage
from Queries as q join 
(select query_name, rating/position as indQuality,
 CASE 
        WHEN rating < 3 THEN 1
        ELSE 0
    END AS qualityPerc 
    from Queries) as q2 on q.query_name = q2.query_name
group by q.query_name;