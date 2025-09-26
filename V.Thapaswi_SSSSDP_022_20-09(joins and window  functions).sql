create database emp;

use emp;

create table employees(
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
dept_id INT,
project_id INT,
manager_id INT 
);

INSERT INTO employees (emp_id, emp_name, dept_id, project_id, manager_id) VALUES
(1, 'Nitya',   1, 100, NULL),
(2, 'ramu',    1, 101, 1),
(3, 'sita',    2, 100, 1),
(4, 'sudha',   3, 102, 2),
(5, 'sai',     4, NULL, 3);


create table departments(
dept_id INT primary key,
dept_name VARCHAR(50),
location VARCHAR(50)
);

INSERT INTO Departments (dept_id, dept_name, location) VALUES
(1, 'HR',        'New York'),
(2, 'Finance',   'germany'),
(3, 'IT',        'netherlands'),
(5, 'Marketing', 'seattle');


create table projects(
project_id INT PRIMARY KEY,
dept_id INT,
project_name VARCHAR(50)
);

INSERT INTO Projects (project_id, dept_id, project_name) VALUES
(100, 2, 'Budgeting'),
(101, 1, 'Recruitment'),
(102, 3, 'Migration'),
(103, 5, 'Campaign');



create table sales(
sale_id INT PRIMARY KEY,
emp_id INT,
sale_date DATE,
sale_amount INT
);

INSERT INTO sales(sale_id,emp_id,sale_date,sale_amount) VALUES
(1,2,'2025-01-01',500),
(2,2,'2025-01-05',700),
(3,2,'2025-01-10',400),
(4,3,'2025-01-03',600),
(5,3,'2025-01-07',800),
(6,4,'2025-01-12',750),
(7,4,'2025-01-04',300),
(8,5,'2025-01-08',450),
(9,5,'2025-01-06',900),
(10,1,'2025-01-11',1200);


-- 1.retrieve all employees along with their departments names
select e.emp_id,e.emp_name,d.dept_name from employees e join departments d on e.dept_id=d.dept_id;

-- 2. List all employees and the projects they are working on (show NULL if no project).
select e.emp_id,e.emp_name,p.project_name from employees e left join projects p on e.project_id=p.project_id;

-- 3. Show all departments and employees (include departments with no employees).
select d.dept_id,d.dept_name,e.emp_name from departments d left join employees e on d.dept_id=e.dept_id;

-- 4. Show all projects and employees working on them (include projects without employees).
select p.project_id,p.project_name,e.emp_name from projects p left join employees e on p.project_id=e.project_id;

-- 5. Retrieve employees along with both department and project details.
select e.emp_id,e.emp_name,d.dept_name,p.project_name 
from employees e 
left join departments d on e.dept_id=d.dept_id
left join projects p on e.project_id=p.project_id;

-- 6. Find employees who are working on projects belonging to a different department than their own.
select e.emp_id,e.emp_name,d.dept_name as emp_dept,p.project_name,d2.dept_name as project_dept 
from employees e join departments d on e.dept_id=d.dept_id
join projects p on e.project_id=p.project_id
join departments d2 on p.dept_id=d2.dept_id 
where e.dept_id <> p.dept_id;

-- 7. List all employees along with their manager's name (self-join).
select e.emp_name as employees,m.emp_name as manager from employees e left join employees m on e.manager_id=m.emp_id;

-- 8. Show the number of employees working in each department.
select d.dept_name, count(e.emp_id) as num_employees from departments d left join employees e on d.dept_id=e.dept_id group by d.dept_name;

-- 9. Show the departments which do not have any employees.
select d.dept_id,d.dept_name from departments d left join employees e on d.dept_id=e.dept_id
where e.emp_id is null;

-- 10. Generate all possible combinations of department and project names (cross join).
select d.dept_name,p.project_name from departments d cross join projects p;

-- Window Functions

-- 1. For each employee's sales, show the previous sale amount (using LAG).
select emp_id,sale_id,sale_date, sale_amount, LAG(sale_amount) 
over (partition by emp_id order by sale_date) as prev_sale from sales;

-- 2. For each employee's sales, show the next sale amount (using LEAD).
select emp_id,sale_id,sale_date,sale_amount, LEAD(sale_amount)
over (partition by emp_id order by sale_date) as next_sale from sales;

-- 3. Show the difference between each employee's current sale and their previous sale.
select emp_id,sale_id,sale_date,sale_amount,sale_amount-LAG(sale_amount)
over(partition by emp_id order by sale_date) as diff_from_prev from sales;

-- 4. Assign a row number to each sale of every employee ordered by sale_date.
select emp_id,sale_id,sale_date,sale_amount, row_number() 
over (partition by emp_id order by sale_date) as row_num from sales;

-- 5. Find the highest sale made by each employee using a window function (not GROUP BY).
select emp_id,sale_id,sale_date,sale_amount, max(sale_amount)
over (partition by emp_id) as max_sale from sales;
