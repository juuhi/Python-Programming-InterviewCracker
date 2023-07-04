-- The ideal time between when a customer places an order and when the order is delivered is below or equal to 45 minutes.


-- You have been tasked with evaluating delivery driver performance by calculating the average order value for each delivery driver who has delivered at least once within this 45-minute period.


-- Your output should contain the driver ID along with their corresponding average order value.

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


################################

Select driver_id, avg(order_total) as avg_total
from delivery_details
where driver_id in
(Select distinct(driver_id)
from delivery_details
where timestampdiff(minute, customer_placed_order_datetime, delivered_to_consumer_datetime) <= 45)
group by 1
