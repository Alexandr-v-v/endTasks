
select cus.name, cus.city, count(*) as total_shipped_orders
from customers as cus inner join orders as ord 
by cus.customer_id = ord.customer_id
group by cus.name, cus.city
where ord.status = "shipped" and total_shipped_orders > 200
order by desc total_shipped_orders

