-- The company you work for has asked you to look into the average order value per hour during rush hours in the San Jose area. Rush hour is from 15H - 17H inclusive.


-- You have also been told that the column order_total represents the gross order total for each order. Therefore, you'll need to calculate the net order total.


-- The gross order total is the total of the order before adding the tip and deducting the discount and refund.


-- Use the column customer_placed_order_datetime for your calculations.

-- delivery_details

-- customer_placed_order_datetime:
-- placed_order_with_restaurant_datetime:
-- driver_at_restaurant_datetime:
-- delivered_to_consumer_datetime:
-- driver_id:
-- restaurant_id:
-- consumer_id:
-- is_new:
-- delivery_region:
-- is_asap:
-- order_total:
-- discount_amount:
-- tip_amount:
-- refunded_amount:

###################################


Select order_hour, avg_earnings
from
(Select HOUR(customer_placed_order_datetime) AS order_hour, avg(order_total + tip_amount - (discount_amount + refunded_amount)) AS avg_earnings
from delivery_details
where delivery_region = 'San Jose'
group by HOUR(customer_placed_order_datetime))t
where order_hour between 15 and 17
