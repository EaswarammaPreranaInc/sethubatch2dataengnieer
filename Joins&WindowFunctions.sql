-- SQL Assignment: Joins & Window Functions

CREATE DATABASE IF NOT EXISTS Joins;

USE Joins;

/*
Employees
Column	Description
emp_id	Unique ID for each employee
emp_name	Employee name
dept_id	Department where the employee works
project_id	Project assigned to the employee
manager_id	Manager of the employee (self join key)
*/


CREATE TABLE Employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(100) NOT NULL,
    dept_id INT,
    project_id INT,
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Employees(emp_id) 
);

INSERT INTO Employees (emp_name, dept_id, project_id, manager_id) VALUES
('John Smith', 1, 101, NULL),
('Alice Johnson', 1, 101, 1),
('Mark Brown', 2, 102, 1),
('Sophia Davis', 2, 103, 3),
('David Wilson', 3, 104, 1),
('Emma Thomas', 3, 104, 5),
('Michael Lee', 1, 101, 1),
('Olivia Martinez', 2, 102, 3),
('Liam Garcia', 3, 105, 5),
('Noah Anderson', 1, 101, 1),
('Ava Thompson', 2, 103, 3),
('William Hernandez', 3, 105, 5),
('Isabella Moore', 1, 102, 1),
('James Taylor', 2, 103, 3),
('Mia Jackson', 3, 104, 5);


/*
Departments
Column	Description
dept_id	Unique ID for each department
dept_name	Department name
location	City where the department is located
*/

CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100),
    location VARCHAR(100)
);

INSERT INTO Departments (dept_id, dept_name, location) VALUES
(1, 'HR', 'New York'),
(2, 'IT', 'San Francisco'),
(3, 'Sales', 'Chicago'),
(4, 'Marketing', 'Los Angeles'),
(5, 'Finance', 'Boston');


/*
Projects
Column	Description
project_id	Unique ID for each project
dept_id	Department responsible for the project
project_name	Project name
*/

CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    dept_id INT,
    project_name VARCHAR(100),
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

INSERT INTO Projects (project_id, dept_id, project_name) VALUES
(101, 1, 'Recruitment Drive'),
(102, 2, 'Website Upgrade'),
(103, 2, 'Mobile App Development'),
(104, 3, 'Sales Campaign'),
(105, 3, 'Customer Outreach'),
(106, 4, 'Ad Campaign'),
(107, 4, 'Brand Awareness'),
(108, 5, 'Budget Planning');


/*
Sales
Column	Description
sale_id	Unique ID for each sale
emp_id	Employee who made the sale
sale_date	Date of the sale
sale_amount	Amount of the sale
*/

CREATE TABLE Sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT,
    sale_date DATE,
    sale_amount DECIMAL(10,2),
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);

INSERT INTO Sales (emp_id, sale_date, sale_amount) VALUES
(5, '2025-09-01', 1200.50),
(6, '2025-09-02', 950.00),
(9, '2025-09-03', 1500.75),
(12, '2025-09-04', 2000.00),
(15, '2025-09-05', 1750.25),
(7, '2025-09-06', 1350.50),
(8, '2025-09-07', 1100.00),
(10, '2025-09-08', 1450.75),
(13, '2025-09-09', 2100.00),
(14, '2025-09-10', 1600.25);


-- Part A – JOINS (10 Questions)

-- 1.	Retrieve all employees along with their department names.

SELECT e.emp_name, d.dept_name
FROM Employees e
INNER JOIN Departments d ON e.dept_id = d.dept_id;

-- 2.	List all employees and the projects they are working on (show NULL if no project).

SELECT e.emp_name, p.project_name
FROM Employees e
LEFT JOIN Projects p ON e.project_id = p.project_id;

-- 3.	Show all departments and employees (include departments with no employees).

SELECT d.dept_name, e.emp_name
FROM Departments d
LEFT JOIN Employees e ON e.dept_id = d.dept_id;

-- 4.	Show all projects and employees working on them (include projects without employees).

SELECT p.project_name, e.emp_name
FROM Projects p
LEFT JOIN Employees e ON e.project_id = p.project_id;

-- 5.	Retrieve employees along with both department and project details.

SELECT e.emp_name, d.dept_name, p.project_name
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id
LEFT JOIN Projects p ON e.project_id = p.project_id;

-- 6.	Find employees who are working on projects belonging to a different department than their own.

SELECT e.emp_name, e.dept_id AS Employee_Dept, p.dept_id AS Project_Dept, p.project_name
FROM Employees e
INNER JOIN Projects p ON e.project_id = p.project_id
WHERE e.dept_id <> p.dept_id;

-- 7.	List all employees along with their manager’s name (self-join).

SELECT e.emp_name AS Employee, m.emp_name AS Manager
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.emp_id;

-- 8.	Show the number of employees working in each department.

SELECT d.dept_name, COUNT(e.emp_id) AS Employee_Count
FROM Departments d
LEFT JOIN Employees e ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

-- 9.	Show the departments which do not have any employees.

SELECT d.dept_name
FROM Departments d
LEFT JOIN Employees e ON e.dept_id = d.dept_id
WHERE e.emp_id IS NULL;

-- 10.	Generate all possible combinations of department and project names (cross join).

SELECT d.dept_name, p.project_name
FROM Departments d
CROSS JOIN Projects p;


-- Part B – Window Functions (5 Questions)

-- 1.	For each employee’s sales, show the previous sale amount (using LAG).

SELECT sale_id, emp_id, sale_amount,
       LAG(sale_amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS Previous_Sale
FROM Sales;

-- 2.	For each employee’s sales, show the next sale amount (using LEAD).

SELECT sale_id, emp_id, sale_amount,
       LEAD(sale_amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS Next_Sale
FROM Sales;

-- 3.	Show the difference between each employee’s current sale and their previous sale.

SELECT sale_id, emp_id, sale_amount,
       sale_amount - LAG(sale_amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS Difference
FROM Sales;

-- 4.	Assign a row number to each sale of every employee ordered by sale_date.

SELECT sale_id, emp_id, sale_amount,
       ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY sale_date) AS Row_Num
FROM Sales;

-- 5.	Find the highest sale made by each employee using a window function (not GROUP BY).

SELECT sale_id, emp_id, sale_amount,
       MAX(sale_amount) OVER (PARTITION BY emp_id) AS Highest_Sale
FROM Sales;