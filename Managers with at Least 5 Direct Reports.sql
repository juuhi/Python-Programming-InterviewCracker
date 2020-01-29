CREATE TABLE Employee.Employee1(
		Id int,
        Name varchar(50),
        Department Varchar(50),
        ManagerId int);
        
INSERT INTO Employee.Employee1 (Id, Name, Department, ManagerId) VALUES (101,'John','A',null);
INSERT INTO Employee.Employee1 (Id, Name, Department, ManagerId) VALUES (102,'Dan','A',101);
INSERT INTO Employee.Employee1 (Id, Name, Department, ManagerId) VALUES (103,'James','A',101);
INSERT INTO Employee.Employee1 (Id, Name, Department, ManagerId) VALUES (104,'Amy','A',101);
INSERT INTO Employee.Employee1 (Id, Name, Department, ManagerId) VALUES (105,'Anne','A',101);
INSERT INTO Employee.Employee1 (Id, Name, Department, ManagerId) VALUES (106,'Ron','B',101);

Select * from Employee1;

# Employee with no manager (It can be employee that are manager (means they donts have manager id)
Select *
From Employee1
Where ManagerId is Null;

# Manager with 5 or more employees under him/her (Managers with at Least 5 Direct Reports)

Select Name
From Employee1
Where Id IN (Select ManagerId
From Employee1
Group By ManagerId
Having Count(ManagerId) > 4);
