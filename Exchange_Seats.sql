Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.
 

Mary wants to change seats for the adjacent students.
 

Can you write a SQL query to output the result for Mary?
 

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:
 

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
Note:
If the number of students is odd, there is no need to change the last one's seat.

##################################  

# If the student id is even then subtract 1 from the id
# If the student id is odd then add 1 to the id
# if the max id is odd then don't change the id
# order by the id

SELECT 
       CASE
        WHEN id % 2 = 0 THEN id-1
        WHEN id % 2 != 0 AND id != (SELECT COUNT(*) from seat) then id+1
        ELSE id
        END as id, student
FROM seat
ORDER BY id;
