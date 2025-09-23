show databases;
use charan;
show tables;
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100) NOT NULL,
    dept_id INT NOT NULL,
    project_id INT,
    manager_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id),
    FOREIGN KEY (manager_id) REFERENCES Employees(emp_id)
) ENGINE=InnoDB;


CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL
) ENGINE=InnoDB;


CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    dept_id INT NOT NULL,
    project_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
) ENGINE=InnoDB;


CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    emp_id INT NOT NULL,
    sale_date DATE NOT NULL,
    sale_amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
) ENGINE=InnoDB;
desc Employees;
desc Departments;
desc Projects;
desc Sales;


INSERT INTO Departments (dept_id, dept_name, location) VALUES
(10, 'HR',        'New York'),
(20, 'Finance',   'London'),
(30, 'IT',        'New York'),
(40, 'Sales',     'Chicago'),
(50, 'Marketing', 'Chicago');

INSERT INTO Projects (project_id, dept_id, project_name) VALUES
(100, 20, 'Budgeting'),
(101, 10, 'Recruitment'),
(102, 30, 'Migration'),
(103, 50, 'Campaign'),
(104, 40, 'Client Acquisition');

INSERT INTO Employees (emp_id, emp_name, dept_id, project_id, manager_id) VALUES
(1, 'Alice',   10, 101, NULL),   -- Manager
(2, 'Bob',     10, 101, 1),      -- Reports to Alice
(3, 'Charlie', 20, 100, 1),      -- Reports to Alice
(4, 'David',   30, 102, 2),      -- Reports to Bob
(5, 'Eve',     40, NULL, 3),     -- No project
(6, 'Frank',   50, 103, 3),      -- Reports to Charlie
(7, 'Grace',   20, 104, 1),      -- Working on project from different dept
(8, 'Hannah',  30, NULL, 4);     -- IT dept, no project

INSERT INTO Sales (sale_id, emp_id, sale_date, sale_amount) VALUES
(1, 2, '2025-01-01', 500),
(2, 2, '2025-01-05', 700),
(3, 2, '2025-01-10', 400),
(4, 3, '2025-01-03', 600),
(5, 3, '2025-01-07', 800),
(6, 3, '2025-01-12', 750),
(7, 5, '2025-01-04', 300),
(8, 5, '2025-01-08', 450),
(9, 6, '2025-01-06', 900),
(10, 6, '2025-01-11', 1200);
select * from Employees;
select * from Departments;
select * from Sales;
select * from Projects;

# Part A – JOINS
## 1. Retrieve all employees along with their department names.

SELECT e.emp_id, e.emp_name, d.dept_name
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id;
-- Inner join gives only employees who have a department assigned

# 2. List all employees and the projects they are working on (show NULL if no project).

SELECT e.emp_id, e.emp_name, p.project_name
FROM Employees e
LEFT JOIN Projects p ON e.project_id = p.project_id;
-- LEFT JOIN ensures employees with no project are included (projects may be NULL)

## 3. Show all departments and employees (include departments with no employees).

SELECT d.dept_id, d.dept_name, e.emp_id, e.emp_name
FROM Departments d
LEFT JOIN Employees e ON d.dept_id = e.dept_id;
-- LEFT JOIN so every department appears, even if no employee is assigned

## 4. Show all projects and employees working on them (include projects without employees).

SELECT p.project_id, p.project_name, e.emp_id, e.emp_name
FROM Projects p
LEFT JOIN Employees e ON p.project_id = e.project_id;
-- LEFT JOIN ensures every project is listed, even with zero employees

## 5. Retrieve employees along with both department and project details.

SELECT e.emp_id, e.emp_name, d.dept_name, p.project_name
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id
LEFT JOIN Projects p ON e.project_id = p.project_id;
-- Both joins ensure all combinations are included, even if project or department is NULL

## 6. Find employees who are working on projects belonging to a different department than their own.

SELECT e.emp_id, e.emp_name, e.dept_id AS emp_dept, p.dept_id AS project_dept
FROM Employees e
JOIN Projects p ON e.project_id = p.project_id
WHERE e.dept_id <> p.dept_id;
-- Only employees with a project, showing mismatched departments

## 7. List all employees along with their manager's name (self-join).

SELECT e.emp_id, e.emp_name, m.emp_name AS manager_name
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.emp_id;
-- Self-join on manager_id; shows NULL for employees with no manager (top-level)

## 8. Show the number of employees working in each department.

SELECT d.dept_id, d.dept_name, COUNT(e.emp_id) AS num_employees
FROM Departments d
LEFT JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name;
-- Groups by department, counts employees (0 if none)

## 9. Show the departments which do not have any employees.

SELECT d.dept_id, d.dept_name
FROM Departments d
LEFT JOIN Employees e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;
-- Only departments with no assigned employees

## 10. Generate all possible combinations of department and project names (cross join).

SELECT d.dept_name, p.project_name
FROM Departments d
CROSS JOIN Projects p;
-- Every department matches to every project




# Part B – WINDOW FUNCTIONS

## 1. For each employee’s sales, show the previous sale amount (using LAG).

SELECT emp_id,sale_id,sale_date,sale_amount,
  LAG(sale_amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS prev_sale
FROM Sales;
-- LAG() gets previous sale for each employee (by date)


## 2. For each employee’s sales, show the next sale amount (using LEAD).

SELECT
  emp_id,
  sale_id,
  sale_date,
  sale_amount,
  LEAD(sale_amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS next_sale 
  FROM Sales;
-- LEAD() gets next sale for each employee (by date)


## 3. Show the difference between each employee’s current sale and their previous sale.

SELECT
  emp_id,
  sale_id,
  sale_date,
  sale_amount,
  sale_amount - LAG(sale_amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS diff_from_prev
FROM Sales;
-- Subtracts previous sale from current (per employee)

## 4. Assign a row number to each sale of every employee ordered by sale_date.

SELECT
  emp_id,
  sale_id,
  sale_date,
  sale_amount,
  ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY sale_date) AS sale_row
FROM Sales;
-- Numbers sales per employee by date

## 5. Find the highest sale made by each employee using a window function (not GROUP BY).

SELECT
  emp_id,
  sale_id,
  sale_date,
  sale_amount,
  MAX(sale_amount) OVER (PARTITION BY emp_id) AS max_sale_per_emp
FROM Sales;
-- Shows max sale for each employee alongside all records (no GROUP BY)
