Total Shipment Weight
Calculate the total weight for each shipment and add it as a new column. 
Your output needs to have all the existing rows and columns in addition to the  
new column that shows the total weight for each shipment. One shipment can have multiple rows.

amazon_shipment
shipment_id 
sub_id 
weight 
shipment_date 



####################### Solution ##########################


Select *, sum(weight) over(partition by shipment_id) as total_weight
from amazon_shipment
