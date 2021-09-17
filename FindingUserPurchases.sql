Write a query that'll identify returning active users. 
A returning active user is a user that has made a second purchase within 7 days of any other of their purchases. 
Output a list of user_ids of these returning active users.


amazon_transactions
id
user_id 
item
created_at    (datetime)
revenue


####################################### Solution ######################


Select Distinct a.user_id
from amazon_transactions as a
join amazon_transactions as b
on a.user_id = b.user_id
where a.id != b.id
and b.created_at >= a.created_at
and b.created_at <= a.created_at + INTERVAL '7 day'
