CREATE TABLE EmpGenders(
        id int (20),
        Name varchar(50),
        Gender varchar(50)
    );

INSERT INTO EmpGenders (id, Name, Gender) VALUES (1, 'Manish', 'Male');

INSERT INTO EmpGenders (id, Name, Gender) VALUES (2, 'Nayak', 'Male');

INSERT INTO EmpGenders (id, Name, Gender) VALUES (3, 'Marti', 'Male');

INSERT INTO EmpGenders (id, Name, Gender) VALUES (4, 'Roy', 'Male');

INSERT INTO EmpGenders (id, Name, Gender) VALUES (5, 'Hardik', 'Male');

INSERT INTO EmpGenders (id, Name, Gender) VALUES (6, 'Manisha', 'Female');

INSERT INTO EmpGenders (id, Name, Gender) VALUES (7, 'Kruti', 'Female');

INSERT INTO EmpGenders (id, Name, Gender) VALUES (8, 'Maria', 'Female')


select *
from empgenders
ORDER BY ROW_NUMBER() OVER(partition by gender order by id), gender desc;


# gender : partition by
f 1
f 2
f 3
m 1
m 2
m 3
m 4

# order by row number over

f 1
m 1
f 2
m 2
f 3
m 3
m 4

# row_number() over(partition by ... order by ....)

# gender desc

m
f
m
f



