-- Write your query below
select u.name,Coalesce(SUM(r.distance),0) as travelled_distance
from users u left join rides r
on u.id = r.user_id
group by u.name
order by travelled_distance desc;