# Select employee name, managerID, and number of employees in the department

create table amazon.manager(
ID int,
Name varchar(20),
Mgr_id int,
deptId int);


insert into amazon.manager(ID,Name,Mgr_id,deptId) Values(1,'John',3,10);
insert into amazon.manager(ID,Name,Mgr_id,deptId) Values(2,'Smith',3,10);
insert into amazon.manager(ID,Name,Mgr_id,deptId) Values(3,'Jane',4,20);

Select * from manager;

WITH d_count As 
(Select deptID, count(*) as d_count
from manager
group by deptId)
Select e.name as Manager_name, m.name as Employee_Name, dc.deptId, dc.d_count as numberofemployees
from manager as m join manager as e right join d_count as dc 
on m.mgr_id = e.ID
and dc.deptId = m.deptId;
