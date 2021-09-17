Customer Orders and Details
Find the number of orders, the number of customers, and the total cost of orders for each city. 
Only include cities that have made at least 5 orders and count all customers in each city even if they did not place an order.

Output each calculation along with the corresponding city name.

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


###################################################### Solution ################################

Select city, count(distinct o.id) as num_orders, count(distinct c.id) as num_customer, sum(total_order_cost)
from customers as c left join orders as o
on c.id = o.cust_id
group by c.city
having count(o.id) >= 5
