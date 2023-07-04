-- Find all employees who are have a job title that includes manager.


-- Output the first name along with the corresponding title.

-- worker

-- worker_id:
-- first_name:
-- last_name:
-- salary:
-- joining_date:
-- department:

-- title

-- worker_ref_id:
-- worker_title:
-- affected_from:

###########################

Select w.first_name, t.worker_title
from title as t
join worker as w
on t.worker_ref_id = w.worker_id
where worker_title LIKE '%manager%'


