Table: Customers

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
+---------------+---------+
customer_id is the primary key for this table.
This table contains information about the customers.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| customer_id   | int     |
| product_id    | int     |
+---------------+---------+
order_id is the primary key for this table.
This table contains information about the orders made by customer_id.
No customer will order the same product more than once in a single day.
 

Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
| price         | int     |
+---------------+---------+
product_id is the primary key for this table.
This table contains information about the products.
 

Write an SQL query to find the most frequently ordered product(s) for each customer.

The result table should have the product_id and product_name for each customer_id who ordered at least one order.

Return the result table in any order.

The query result format is in the following example.

#############################################################################

# We use group by reason, we used count on one dimention and other dimention should be grouped with the previous one.


Select product_id, product_name, customer_id
from 
(Select o.product_id, p.product_name, o.customer_id, 
dense_rank() over(partition by o.customer_id order by count(o.product_id) desc) as rnk
from Orders as o
join Products as p
on o.product_id = p.product_id
group by o.customer_id, o.product_id)temp
where rnk = 1

