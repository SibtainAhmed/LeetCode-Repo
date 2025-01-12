# Write your MySQL query statement below

with DayAmount as (select visited_on, sum(amount) 'total' from Customer group by visited_on)

select visited_on, amount, average_amount from (
    select visited_on,
    sum(total) over(order by visited_on ASC rows between 6 preceding and current row) AS 'amount',
round(avg(total) over(order by visited_on ASC rows between 6 preceding and current row), 2) AS 'average_amount'
    from DayAmount ) as temp
where  DATE_SUB(visited_on, INTERVAL 6 DAY) in (select visited_on from dayAmount) 
order by visited_on asc;