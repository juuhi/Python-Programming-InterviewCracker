User Growth Rate
Find the growth rate of active users for Dec 2020 to Jan 2021 for each account. 
The growth rate is defined as the number of users in January 2021 divided by the number of users in Dec 2020. Output the account_id and growth rate.

sf_events

date 
account_id
user_id

########################################### Solution ##############################################



select account_id, cast(cnt_2021 as decimal)/cnt_2020 as growth_rate
from 
(Select account_id, count(distinct case when extract(MONTH from date) = 12 and extract(YEAR from date) = 2020 then user_id end) as cnt_2020,
count(distinct case when extract(MONTH from date) = 1 and extract(YEAR from date) = 2021 then user_id end) as cnt_2021
from sf_events
group by 1)as iq

