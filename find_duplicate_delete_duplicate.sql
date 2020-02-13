CREATE TABLE contacts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL, 
    email VARCHAR(255) NOT NULL
);

INSERT INTO contacts (first_name,last_name,email) 
VALUES ('Carine ','Schmitt','carine.schmitt@verizon.net'),
       ('Jean','King','jean.king@me.com'),
       ('Peter','Ferguson','peter.ferguson@google.com'),
       ('Janine ','Labrune','janine.labrune@aol.com'),
       ('Jonas ','Bergulfsen','jonas.bergulfsen@mac.com'),
       ('Janine ','Labrune','janine.labrune@aol.com'),
       ('Susan','Nelson','susan.nelson@comcast.net'),
       ('Zbyszek ','Piestrzeniewicz','zbyszek.piestrzeniewicz@att.net'),
       ('Roland','Keitel','roland.keitel@yahoo.com'),
       ('Julie','Murphy','julie.murphy@yahoo.com'),
       ('Kwai','Lee','kwai.lee@google.com'),
       ('Jean','King','jean.king@me.com'),
       ('Susan','Nelson','susan.nelson@comcast.net'),
       ('Roland','Keitel','roland.keitel@yahoo.com');
       
select * from contacts
order by email;

# The following query returns the duplicate emails in the contacts table:

select email, count(email), first_name, last_name
from contacts
group by email, first_name, last_name
having count(email) > 1;

##### following query will select the disntict first name and last name of the duplicated rows
select distinct(first_name), last_name
from contacts
where email in (select email
from contacts
group by email
having count(email) > 1);

######## delete the duplicated rows ####### saving the higher ids ### delete the lower values ids
delete c1 
from contacts c1 join contacts c2
on c1.email = c2.email
where c1.id < c2.id;

DELETE FROM contacts 
WHERE 
    id IN (
    SELECT 
        id 
    FROM (
        SELECT 
            id,
            ROW_NUMBER() OVER (
                PARTITION BY email
                ORDER BY email) AS row_num
        FROM 
            contacts
        
    ) t
    WHERE row_num > 1
);

########## find duplicated based on multiple columns ######

SELECT 
    first_name, COUNT(first_name),
    last_name,  COUNT(last_name)
    -- email,      COUNT(email)
FROM
    contacts
GROUP BY 
    first_name , 
    last_name , 
    email
HAVING  COUNT(first_name) > 1
    AND COUNT(last_name) > 1
    -- AND COUNT(email) > 1;
