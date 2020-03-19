# Extract the date year or month or day and applying a condition
create table amazon.date_practice
(id int,
m_date date);

insert into date_practice(id, m_date) values (1,'2015-01-01');
insert into date_practice(id, m_date) values (1,'2016-01-01');
insert into date_practice(id, m_date) values (1,'2017-01-01');

Select * from date_practice;

Select year(m_date) as year_r
from date_practice
where year(m_date) >=2016

-- Select str_to_date(m_date, 'yyyy') as year_r
-- from date_practice
-- where year(m_date) >= 2016;
