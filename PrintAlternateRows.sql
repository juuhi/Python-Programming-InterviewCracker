# Select the alternate rows from the employee1 table:

create table amazon.Employee1(
ID int,
Salary int);

use amazon;

insert into amazon.employee1(ID, Salary)values(10,2000);
insert into amazon.employee1(ID, Salary)values(11,5000);
insert into amazon.employee1(ID, Salary)values(12,3000);

Select * from employee1;
SET @row_number = 0; 
Select * from
(SELECT @row_number:=@row_number + 1 AS num, ID, Salary
FROM employee1)temp
where num%2 = 1
