show databases;
show tables from Employee;

alter table department add column Gender varchar(20);
Create table Department(
Id int,
name varchar(200),
Gender varchar(20),
Salary int,
dept_id int);

Select * from department;

Insert into Department( Id, name, Gender, Salary, dept_id) values (1, "Juhi", "F", 1000, 1);
Insert into Department( Id, name,Gender,Salary, dept_id) values (2, "Ashu", "M", 2000, 2);
Insert into Department( Id, name, Gender,Salary, dept_id) values (3, "Jiohn", "M", 2000, 3);
Insert into Department( Id, name, Gender,Salary, dept_id) values (4, "Juliet", "F", 2000, 1);
Insert into Department( Id, name, Gender,Salary, dept_id) values (5, "Ram", "M", 3000, 2);
Insert into Department( Id, name, Gender,Salary, dept_id) values (6, "Karishma", "F", 4000, 3);
Insert into Department( Id, name, Gender,Salary, dept_id) values (7, "Renal", "M", 1000, 1);
Insert into Department( Id, name, Gender,Salary, dept_id) values (8, "Angela", "F", 50000, 2);
Insert into Department( Id, name, Gender,Salary, dept_id) values (9, "Kareena", "F", 60000, 4);

# This is by the Salary by the department

Select Id, name, Gender, Salary, dept_id
from
(Select Id, name, Gender, Salary, dept_id,
DENSE_RANK() OVER(partition by dept_id order by Salary Desc) as rank_sal
from department) e
where rank_sal <3;

select * from department;

# This is by the gender (top 2 salaries by the gender)(using the window function rank_over()

select * from 
(select Id, name, Gender, Salary, dept_id, dense_rank() over(partition by Gender order by Salary Desc) as rank_Sal
from department) e
where rank_Sal < 3
order by Id desc;
