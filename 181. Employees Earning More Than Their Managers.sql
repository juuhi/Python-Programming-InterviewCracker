SQL Schema
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+

############################# Using the sub query #############

# Write your MySQL query statement below
Select e1.Name as Employee
From Employee as e1
Where Salary > (Select Salary
                from Employee as e2
                Where e1.ManagerId = e2.Id)  # to get the 3 & 4 in the suquery
                
################### Using the self join ####################
                
Select e1.Name as Employee
From Employee as e1 Join Employee as e2
On e1.managerID = e2.Id
Where e1.Salary > e2.Salary
