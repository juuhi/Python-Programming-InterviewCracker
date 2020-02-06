Membership status change from free to paid
We can use the self join and then can extract the data

Show databases;
create table Sales.membership
(Id int,
start_date date,
end_date date,
status varchar(200));

Insert into sales.membership(Id, start_date, end_date, status) values (1, '2019-09-01', '2019,10-01', "Free");
Insert into sales.membership(Id, start_date, end_date, status) values (1, '2019-10-01', '2019,11-01', "Paid");
Insert into sales.membership(Id, start_date, end_date, status) values (2, '2019-11-01', '2019,12-01', "Free");
Insert into sales.membership(Id, start_date, end_date, status) values (2, '2019-12-01', '2020-01-01', "Paid");
Insert into sales.membership(Id, start_date, end_date, status) values (2, '2020-01-01', '2020-09-01', "Premium");

Select * from sales.membership;

use Sales;

Select Id, start_date, end_date, case when status = "Paid" then "Free -> Paid" end as status
from
(Select m2.* from membership as m1 join membership as m2
on m1.id = m2.id
where m1.end_date = m2.start_date
and m2.status = "Paid")e;

Output

Id.  Start_date.  end_date.   status
1,  2019-10-01, 2019-11-01 , Free -> Paid
2,  2019-12-01, 2020-01-01,  Free -> Paid
