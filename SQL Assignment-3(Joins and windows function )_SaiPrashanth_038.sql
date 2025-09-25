-- SQL Assignment 3 Joins and Windows functions

create database joins;
use joins;
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(20),
    dept_id INT,
    project_id INT,
    manager_id INT
);

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(20),
    location VARCHAR(30)
);

CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    dept_id INT,
    project_name VARCHAR(30)
);

CREATE TABLE sales(
	sale_id INT PRIMARY KEY,
	emp_id INT,
	sale_date date,
	sale_amount INT
);

INSERT INTO Departments (dept_id, dept_name, location) 
VALUES(10, 'HR', 'New York'),
(20, 'Finance', 'London'),
(30, 'IT','New York'),
(40, 'Sales','Chicago'),
(50, 'Marketing', 'Chicago');



INSERT INTO Projects (project_id, dept_id, project_name) 
VALUES(100, 20, 'Budgeting'),
(101, 10, 'Recruitment'),
(102, 30, 'Migration'),
(103, 50, 'Campaign'),
(104, 40, 'Client Acquisition');



INSERT INTO Employees (emp_id, emp_name, dept_id, project_id, manager_id) 
VALUES(1, 'Alice',10, 101, NULL),
(2, 'Bob',10, 101, 1),
(3, 'Charlie', 20, 100, 1),
(4, 'David',30, 102, 2),
(5, 'Eve',40, NULL, 3),
(6, 'Frank',50, 103, 3),
(7, 'Grace',20, 104, 1),
(8, 'Hannah', 30, NULL, 4);


INSERT INTO Sales (sale_id, emp_id, sale_date, sale_amount) 
VALUES(1, 2, '2025-01-01', 500),
(2, 2, '2025-01-05', 700),
(3, 2, '2025-01-10', 400),
(4, 3, '2025-01-03', 600),
(5, 3, '2025-01-07', 800),
(6, 3, '2025-01-12', 750),
(7, 5, '2025-01-04', 300),
(8, 5, '2025-01-08', 450),
(9, 6, '2025-01-06', 900),
(10, 6, '2025-01-11', 1200);

-- Joins
-- 1.Retrieve all employees along with their department names.
SELECT e.emp_id, e.emp_name, d.dept_name
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id;

-- 2.List all employees and the projects they are working on (show NULL if no project).
SELECT e.emp_id, e.emp_name, p.project_name
   FROM employees e
   LEFT JOIN projects p ON e.project_id = p.project_id;

-- 3.Show all departments and employees (include departments with no employees).
SELECT d.dept_id, d.dept_name, e.emp_id, e.emp_name
   FROM departments d
   LEFT JOIN employees e ON d.dept_id = e.dept_id;

-- 4.Show all projects and employees working on them (include projects without employees).
SELECT p.project_id, p.project_name, e.emp_id, e.emp_name
   FROM projects p
   LEFT JOIN employees e ON p.project_id = e.project_id;

-- 5.Retrieve employees along with both department and project details.
SELECT e.emp_id, e.emp_name, d.dept_name, p.project_name
   FROM employees e
   JOIN departments d ON e.dept_id = d.dept_id
   LEFT JOIN projects p ON e.project_id = p.project_id;

-- 6.Find employees who are working on projects belonging to a different department than their own.
SELECT e.emp_id, e.emp_name, d.dept_name, p.project_name
   FROM employees e
   JOIN departments d ON e.dept_id = d.dept_id
   LEFT JOIN projects p ON e.project_id = p.project_id
   WHERE p.dept_id != e.dept_id;

-- 7.List all employees along with their manager’s name (self-join).
SELECT e.emp_id, e.emp_name, m.emp_name AS manager_name
   FROM employees e
   LEFT JOIN employees m ON e.manager_id = m.emp_id;

-- 8.Show the number of employees working in each department.
SELECT d.dept_name, COUNT(e.emp_id) AS num_employees
   FROM departments d
   LEFT JOIN employees e ON d.dept_id = e.dept_id
   GROUP BY d.dept_name;


-- 9.Show the departments which do not have any employees.
SELECT d.dept_name
   FROM departments d
   LEFT JOIN employees e ON d.dept_id = e.dept_id
   WHERE e.emp_id IS NULL;

-- 10.Generate all possible combinations of department and project names (cross join).
SELECT d.dept_name, p.project_name
FROM departments d
CROSS JOIN projects p;


-- Window Functions

-- 1.For each employee’s sales, show the previous sale amount (using LAG).
SELECT sale_id, emp_id, sale_date, sale_amount,
          LAG(sale_amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS prev_sale_amount
   FROM sales;

-- 2.For each employee’s sales, show the next sale amount (using LEAD).
SELECT sale_id, emp_id, sale_date, sale_amount,
          LEAD(sale_amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS next_sale_amount
   FROM sales;

-- 3.Show the difference between each employee’s current sale and their previous sale.
SELECT sale_id, emp_id, sale_date, sale_amount,
          sale_amount - LAG(sale_amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS sale_diff
   FROM sales;

-- 4.Assign a row number to each sale of every employee ordered by sale_date.
SELECT sale_id, emp_id, sale_date, sale_amount,
          ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY sale_date) AS row_num
   FROM sales;


-- 5.Find the highest sale made by each employee using a window function (not GROUP BY).
SELECT emp_id, sale_id, sale_amount,
          MAX(sale_amount) OVER (PARTITION BY emp_id) AS highest_sale
   FROM sales;




