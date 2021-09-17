Number of Shipments Per Month
Write a query that will calculate the number of shipments per month. The unique key for one shipment is a combination of shipment_id and sub_id. 
Output the year_month in format YYYY-MM and the number of shipments in that month.

amazon_shipment
shipment_id 
sub_id 
weight 
shipment_date

##################################### Solution ##############################


SELECT to_char(shipment_date, 'YYYY-MM') AS year_month,
       count(*)
FROM amazon_shipment
GROUP BY 1
