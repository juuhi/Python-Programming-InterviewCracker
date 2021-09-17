Total Cost Of Orders
Find the total cost of each customer's orders. Output customer's id, first name, 
and the total order cost. Order records by customer's first name alphabetically.

customers
id 
first_name 
last_name 
city 
address 
phone_number 

orders
id 
cust_id 
order_date 
order_details 
total_order_cost

############################################# Solution ###################################


Select c.id, c.first_name, sum(total_order_cost)
from customers as c join orders as o
on c.id = o.cust_id
group by c.id, c.first_name
order by first_name
