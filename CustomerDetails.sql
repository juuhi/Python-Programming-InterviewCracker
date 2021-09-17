Customer Details
Find the details of each customer regardless of whether the customer made an order. 
Output the customer's first name, last name, and the city along with the order details.
Your output should be listing the customer's orders not necessarily listing the customers. 
This means that you may have duplicate rows in your results due to a customer ordering several of the same items. 
Sort records based on the customer's first name and the order details in ascending order.


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

################################## Solution ###################

Select first_name, last_name, city, order_details
from customers left join orders
on customers.id = orders.cust_id
order by first_name, order_details
