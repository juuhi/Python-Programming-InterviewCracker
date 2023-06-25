Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id is the primary key for this table.
Each row of this table indicates the name of the employee whose ID is employee_id.
 

Table: Salaries

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| salary      | int     |
+-------------+---------+
employee_id is the primary key for this table.
Each row of this table indicates the salary of the employee whose ID is employee_id.
 

Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is missing if:

The employee's name is missing, or
The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.

The query result format is in the following example.


###################################


# Write your MySQL query statement below


# Be careful while selecting the nulls join should have right table with nulls
  
Select e.employee_id
from Employees as e
left join Salaries as s
on e.employee_id = s.employee_id
where salary is null
union
select s.employee_id
from Salaries as s
left join Employees as e
on s.employee_id = e.employee_id
where name is null
order by employee_id
