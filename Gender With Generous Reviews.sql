-- Write a query to find which gender gives a higher average review score when writing reviews as guests. 
-- Use the from_type column to identify guest reviews. 
-- Output the gender and their average review score.


####################################

Select max(rscore), gender
from
(Select gender, avg(review_score) as rscore
from airbnb_guests as ag
join airbnb_reviews as ar
on ag.guest_id = ar.from_user
where from_type = 'guest'
group by gender)t
