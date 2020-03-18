# Select the Second Highest Salary from the employee1 table (1st using the Window function, 2nd using the not! or max function)
create table amazon.Employee1(
ID int,
Salary int);

use amazon;

insert into amazon.employee1(ID, Salary)values(10,2000);
insert into amazon.employee1(ID, Salary)values(11,5000);
insert into amazon.employee1(ID, Salary)values(12,3000);

Select * from employee1;

Select *
from (select *, dense_rank() over(order by Salary) as rank_sal from employee1)temp
where rank_sal = 2;

########

Select max(salary)
from employee1
where salary != (Select max(salary) from employee1);
