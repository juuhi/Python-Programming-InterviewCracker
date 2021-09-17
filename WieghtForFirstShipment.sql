Weight For First Shipment
Write a query to find the weight for each shipment's earliest shipment date. Output the shipment id along with the weight.

amazon_shipment
shipment_id 
sub_id 
weight 
shipment_date

######################### Solution #####################

Select shipment_id, weight from
(select shipment_id, weight, 
row_number() over(partition by shipment_id order by shipment_date)
from amazon_shipment)c
where row_number = 1;
