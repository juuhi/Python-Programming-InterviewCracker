To remain competitive, the company you work with must reduce the number of extremely late deliveries.


A delivery is flagged as extremely late if the actual delivery time is more than 20 minutes (not inclusive) after the predicted delivery time.


You have been asked to calculate the percentage of orders that arrive extremely late each month.


Your output should include the month in the format 'YYYY-MM' and the percentage of extremely late orders as a percentage of all orders placed in that month.


#################################
# Very Good Question to extract the date and identify the case condition and percentage

Select date_format(order_placed_time, "%Y-%m"),
100*(count(case when timestampdiff(minute, predicted_delivery_time, actual_delivery_time)> 20 
     THEN delivery_id end)/count(delivery_id)) as perc 
      from delivery_orders
      group by 1
