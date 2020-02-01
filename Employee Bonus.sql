#Select all employee's name and bonus whose bonus is < 1000.

Table:Employee

+-------+--------+-----------+--------+
| empId |  name  | supervisor| salary |
+-------+--------+-----------+--------+
|   1   | John   |  3        | 1000   |
|   2   | Dan    |  3        | 2000   |
|   3   | Brad   |  null     | 4000   |
|   4   | Thomas |  3        | 4000   |
+-------+--------+-----------+--------+
empId is the primary key column for this table.
Table: Bonus

+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
empId is the primary key column for this table.
Example ouput:

+-------+-------+
| name  | bonus |
+-------+-------+
| John  | null  |
| Dan   | 500   |
| Brad  | null  |
+-------+-------+

############## Again to handle the Null values #########

The output to run this code with the sample data is as below.

| name   | bonus |
|--------|-------|
| Dan    | 500   |
| Thomas | 2000  |
| Brad   |       |
| John   |       |
The bonus value for 'Brad' and 'John' is empty, which is actually NULL in the database. "Conceptually, NULL means “a missing unknown value” and it is treated somewhat differently from other values." Check the Working with NULL Values in MySQL manual for more details. In addition, we have to use IS NULL or IS NOT NULL to compare a value with NULL.

At last, we can add a WHERE clause with the proper conditions to filter these records.


##############

Select e.name
From Employee as e left join Bonus as b
On e.empId = b.empId
Where b.bonus < 1000 or bonus IS NULL;

