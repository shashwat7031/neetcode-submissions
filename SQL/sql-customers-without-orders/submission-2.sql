-- Write your query below
select customers.name as name 
from customers left join orders
on customers.id = orders.customer_id
where orders.id is Null;