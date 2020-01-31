#Query the customer_number from the orders table for the customer who has placed the largest number of orders.

#It is guaranteed that exactly one customer will have placed more orders than any other customer.

#The orders table is defined as follows:

REATE DATABASE Sales;
DROP TABLE IF EXISTS Sales.Orders;
CREATE TABLE Sales.Orders(
		order_number int NOT NULL auto_increment,
        customer_number int,
        order_date date,
        required_date date,
        shipped_date date,
        status char(15),
        comment char(200),
        PRIMARY KEY (order_number)
        );
Update Sales.Orders
Set customer_number = 3
Where customer_number = 4;

# To delete a row from the table
Delete
from Sales.Orders
Where order_number = 5;
        
INSERT INTO Sales.Orders (order_number, customer_number, order_date, required_date, shipped_date, status, comment) VALUES (1, 1, '2017-04-09', '2017-04-13', '2017-04-12' , 'Closed', null);
INSERT INTO Sales.Orders (order_number, customer_number, order_date, required_date, shipped_date, status, comment) VALUES (2, 2, '2017-04-15', '2017-04-20', '2017-04-18', 'Closed', null);
INSERT INTO Sales.Orders (order_number, customer_number, order_date, required_date, shipped_date, status, comment) VALUES (3, 3, '2017-04-16', '2017-04-25', '2017-04-20', 'Closed', null);
INSERT INTO Sales.Orders (order_number, customer_number, order_date, required_date, shipped_date, status, comment) VALUES (4, 3, '2017-04-18', '2017-04-28', '2017-04-25', 'Closed', null);
INSERT INTO Sales.Orders (order_number, customer_number, order_date, required_date, shipped_date, status, comment) VALUES (5, 3, '2017-04-19', '2017-04-29', '2017-04-26', 'Closed', null);
INSERT INTO Sales.Orders (order_number, customer_number, order_date, required_date, shipped_date, status, comment) VALUES (6, 4, '2017-04-20', '2017-04-29', '2017-04-26', 'Closed', null);
INSERT INTO Sales.Orders (order_number, customer_number, order_date, required_date, shipped_date, status, comment) VALUES (7, 4, '2017-04-22', '2017-04-29', '2017-04-26', 'Closed', null);
INSERT INTO Sales.Orders (order_number, customer_number, order_date, required_date, shipped_date, status, comment) VALUES (8, 4, '2017-04-23', '2017-04-29', '2017-04-26', 'Closed', null);

Select * from Sales.Orders;

#######################

| order_number | customer_number | order_date | required_date | shipped_date | status | comment |
|--------------|-----------------|------------|---------------|--------------|--------|---------|
| 1            | 1               | 2017-04-09 | 2017-04-13    | 2017-04-12   | Closed |         |
| 2            | 2               | 2017-04-15 | 2017-04-20    | 2017-04-18   | Closed |         |
| 3            | 3               | 2017-04-16 | 2017-04-25    | 2017-04-20   | Closed |         |
| 4            | 3               | 2017-04-18 | 2017-04-28    | 2017-04-25   | Closed |         |


'1','1','2017-04-09','2017-04-13','2017-04-12','Closed',NULL
'2','2','2017-04-15','2017-04-20','2017-04-18','Closed',NULL
'3','3','2017-04-16','2017-04-25','2017-04-20','Closed',NULL
'4','3','2017-04-18','2017-04-28','2017-04-25','Closed',NULL
'5','3','2017-04-19','2017-04-29','2017-04-26','Closed',NULL
'6','4','2017-04-20','2017-04-29','2017-04-26','Closed',NULL
'7','4','2017-04-22','2017-04-29','2017-04-26','Closed',NULL
'8','4','2017-04-23','2017-04-29','2017-04-26','Closed',NULL


#################


Select * from Sales.Orders;

# Maximum purchase customer
Use Sales;

Select Customer_Number, count(order_number) as rm
from Orders
Group By Customer_Number
Order by rm desc;

# If customer have the same number of orders
Select Customer_number
from orders
group by customer_number
having count(order_number) = (Select Max(numberoforders)
							  from 
                              (Select customer_number, count(order_number) as numberoforders
                              from orders
                              group by customer_number) as temp);

