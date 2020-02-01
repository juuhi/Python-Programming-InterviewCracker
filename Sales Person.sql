CREATE TABLE Sales.salesperson(
        sales_id int not null auto_increment,
        name varchar(200),
        salary int,
        commission_rate int,
        hire_date date,
		primary key (sales_id)
    );
    
INSERT INTO Sales.salesperson(sales_id, name, salary, commission_rate, hire_date) Values (1, 'John', 100000, 6, '2006-04-01');
INSERT INTO Sales.salesperson(sales_id, name, salary, commission_rate, hire_date) Values (2, 'Amy', 120000, 5, '2010-05-01');
INSERT INTO Sales.salesperson(sales_id, name, salary, commission_rate, hire_date) Values (3, 'Mark', 65000, 12, '2008-12-25');
INSERT INTO Sales.salesperson(sales_id, name, salary, commission_rate, hire_date) Values (4, 'Pam', 25000, 25, '2005-01-01');
INSERT INTO Sales.salesperson(sales_id, name, salary, commission_rate, hire_date) Values (5, 'Alex', 50000, 10, '2007-02-03');

 sales_id | name | salary | commission_rate | hire_date |
+----------+------+--------+-----------------+-----------+
|   1      | John | 100000 |     6           | 4/1/2006  |
|   2      | Amy  | 120000 |     5           | 5/1/2010  |
|   3      | Mark | 65000  |     12          | 12/25/2008|
|   4      | Pam  | 25000  |     25          | 1/1/2005  |
|   5      | Alex | 50000  |     10          | 2/3/2007  |

Select * from Sales.salesperson;

order
+----------+------------+---------+----------+--------+
| order_id | order_date | com_id  | sales_id | amount |
+----------+------------+---------+----------+--------+
| 1        |   1/1/2014 |    3    |    4     | 100000 |
| 2        |   2/1/2014 |    4    |    5     | 5000   |
| 3        |   3/1/2014 |    1    |    1     | 50000  |
| 4        |   4/1/2014 |    1    |    4     | 25000  |
+----------+----------+---------+----------+--------+



CREATE TABLE Sales.order(
        order_id int not null auto_increment,
        order_date date,
        com_id int,
        sales_id int,
        amount int,
		primary key (order_id),
        FOREIGN KEY (sales_id) REFERENCES Sales.salesperson(sales_id),
        FOREIGN KEY (com_id) REFERENCES Sales.company(com_id)
        );
# You first have to insert the data into both the referring tables to insert the data into this table, otherwise it will throw an error

INSERT INTO Sales.order(order_id, order_date, com_id, sales_id, amount) values (1, '2014-01-01', 3, 4, 100000);
INSERT INTO Sales.order(order_id, order_date, com_id, sales_id, amount) values (2, '2014-02-01', 4, 5, 5000);
INSERT INTO Sales.order(order_id, order_date, com_id, sales_id, amount) values (3, '2014-03-01', 1, 1, 50000);
INSERT INTO Sales.order(order_id, order_date, com_id, sales_id, amount) values (4, '2014-04-01', 1, 4, 25000);

Select * from Sales.order;

company
+---------+--------+------------+
| com_id  |  name  |    city    |
+---------+--------+------------+
|   1     |  RED   |   Boston   |
|   2     | ORANGE |   New York |
|   3     | YELLOW |   Boston   |
|   4     | GREEN  |   Austin   |
+---------+--------+------------+

DROP TABLE IF EXISTS Sales.company;  # it is not allow you to drop as you gave the foreign key reffering to this table), so you have to alter the
# table and change the datatype

CREATE TABLE Sales.company(
        com_id int not null auto_increment,
        name varchar(200),
        city varchar(200),
		primary key (com_id));

ALTER TABLE Sales.company MODIFY COLUMN name VARCHAR(200);

Select * from Sales.company;

INSERT INTO Sales.company(com_id, name, city) values (1, 'RED', 'Boston');
INSERT INTO Sales.company(com_id, name, city) values (2, 'ORANGE', 'New York');
INSERT INTO Sales.company(com_id, name, city) values (3, 'YELLOW', 'Boston');
INSERT INTO Sales.company(com_id, name, city) values (4, 'GREEN', 'Austin');

select s.sales_id, s.name from sales.salesperson as s join sales.order as o on s.sales_id = o.sales_id;
select * from sales.salesperson as s join sales.order as o on s.sales_id = o.sales_id;
select * from sales.salesperson as s left join sales.order as o on s.sales_id = o.sales_id;

select * from sales.salesperson as s join sales.order as o on s.sales_id = o.sales_id
join company as c on c.com_id = o.com_id
where c.name != 'RED';

# REason for the left join is that so we can get all the sales_id that are selling red
and not in because we do not want the id that are selling for the name "RED"
######

SELECT 
	s.name
FROM 
	salesperson as s
WHERE 
	s.sales_id NOT IN (SELECT 
			o.sales_id
	FROM sales.order as o 
		left join company as c on o.com_id = c.com_id
where c.name = 'RED')
;
