use employee;
-- Joins --
-- 1 Retrieve all employees along with their departments --
select e.emp_id,e.emp_name,d.dept_name from employees e join departments d on e.dept_id = d.dept_id;

-- 2 list all employees and the projects they are working on (show null if no project)
select e.emp_id,e.emp_name,p.project_name from employees e left join project p on e.project_id = p.project_id;

-- 3 show all departments and employees (include departments with no employees) --
select d.dept_id,d.dept_name,e.emp_id,e.emp_name from departments d left join employees e on d.dept_id=e.dept_id order by d.dept_id,e.emp_id;

-- 4 show all projects and employees working on them (include projects without employees) -- 
select p.project_id,p.project_name,e.emp_id,e.emp_name from project p left join employees e on p.project_id = e.project_id order by p.project_id, e.emp_id;

-- 5 retrieve employees along with both department and project details --
select e.emp_id,e.emp_name,d.dept_id,d.dept_name,p.project_id,p.project_name from employees e left join departments d on e.dept_id = d.dept_id left join project p 
on e.project_id = p.project_id order by e.emp_id;

-- 6 find employees who are working on projects belonging to a different department than their own --
select e.emp_id,e.emp_name,d.dept_name as employee_department,p.project_name,dp.dept_name as project_department from employees e join departments d
on e.dept_id=d.dept_id join project p on e.project_id=p.project_id join departments dp 
on p.dept_id=dp.dept_id where e.dept_id<>p.dept_id;

-- 7 list all employees along with their manager's name(self-join) --
select e.emp_id,e.emp_name,m.emp_name as manager_name from employees e left join employees m on e.manager_id = m.emp_id order by e.emp_id;

-- 8 show the number of employees working in each department --
select d.dept_id,d.dept_name,count(e.emp_id) as num_employees from departments d left join employees e on d.dept_id = e.dept_id
group by d.dept_id, d.dept_name order by d.dept_id;

-- 9 show the departments which do not have any employees --
select d.dept_id, d.dept_name from departments d left join employees e
on d.dept_id = e.dept_id where e.emp_id IS NULL;

-- 10 generate all possible combinations of department and project names(cross join) --
select d.dept_name,p.project_name from departments d cross join project p;

-- window functions --
-- 1 for each employee's sales,show the previous sale amount (using LAG) --
select emp_id,sale_date,sale_amount,LAG(sale_amount) over (partition by emp_id order by sale_date) as previous_sale
from sales order by emp_id, sale_date;

-- 2 for each employee's sales,show the next sale amount (using LEAD) --
select emp_id,sale_date,sale_amount,LEAD(sale_amount) over (partition by emp_id order by sale_date) as next_sale_amount
from sales order by emp_id, sale_date;

-- 3 show the difference between each employee's current sale and their previous sale --
select emp_id,sale_date,sale_amount,LAG(sale_amount) over (partition by emp_id order by sale_date) as prev_sale_amount,sale_amount - LAG(sale_amount)
over (partition by emp_id order by sale_date) as difference_from_prev from sales order by emp_id, sale_date;

-- 4 assign a row number to each sale of every employee ordered by sale_date --
select emp_id,sale_date,sale_amount,ROW_NUMBER() over (partition by emp_id order by sale_date) as sale_rank
from sales order by emp_id, sale_date;

-- 5 find the highest sale made by each employee using a window funcion (not group by) --
select emp_id,sale_date,sale_amount,MAX(sale_amount) over (partition by emp_id) as highest_sale
from sales order by emp_id, sale_date;


