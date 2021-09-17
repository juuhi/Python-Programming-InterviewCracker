Favorite Customer
Find "favorite" customers based on the order count and the total cost of orders.
A customer is considered as a favorite if he or she has placed more than 3 orders and with the total cost of orders more than $100.

customers
id 
first_name 
last_name 
cityvar 
address 
phone_number 

orders
id 
cust_id 
order_date 
order_details 
total_order_cost 

####################################### Solution ######################################


Select first_name, city, count(o.id) as order_count, sum(total_order_cost) as total_cost
from customers as c join orders as o
on c.id = o.cust_id
group by cust_id, first_name, city
having count(o.id) > 3 and sum(total_order_cost) > 100


