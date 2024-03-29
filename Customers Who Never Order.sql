Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------

##################### Use NOT EXISTS instead of NOT IN as NOT EXISTS do not return null values while not in does.

select c.Name as Customers
from Customers as c
where NOT EXISTS (Select * from Orders as o where c.Id = o.CustomerId)

########################################
# Write your MySQL query statement below

select Name as Customers
from Customers
where Id not in (select CustomerId
                 from Orders)
                 
      
