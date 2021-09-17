Order Details
Find order details made by Jill and Eva.
Consider the Jill and Eva as first names of customers.
Output the order date, details and cost along with the first name.
Order records based on the customer id in ascending order.


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

################################ Solution ###################


Select first_name, order_date, order_details, total_order_cost
from customers as c join orders as o
on c.id = o.cust_id
where first_name IN ('Jill', 'Eva')
order by cust_id
