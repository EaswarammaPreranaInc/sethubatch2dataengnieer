

-- Part A – JOINS

-- Q1. Retrieve all employees along with their department names.
SELECT e.emp_id, e.emp_name, d.dept_name
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id;

-- Q2. List all employees and the projects they are working on (show NULL if no project).
SELECT e.emp_id, e.emp_name, p.project_name
FROM Employees e
LEFT JOIN Projects p ON e.project_id = p.project_id;

-- Q3. Show all departments and employees (include departments with no employees).
SELECT d.dept_id, d.dept_name, e.emp_name
FROM Departments d
LEFT JOIN Employees e ON d.dept_id = e.dept_id;

-- Q4. Show all projects and employees working on them (include projects without employees).
SELECT p.project_id, p.project_name, e.emp_name
FROM Projects p
LEFT JOIN Employees e ON p.project_id = e.project_id;

-- Q5. Retrieve employees along with both department and project details.
SELECT e.emp_id, e.emp_name, d.dept_name, p.project_name
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id
LEFT JOIN Projects p ON e.project_id = p.project_id;

-- Q6. Find employees who are working on projects belonging to a different department than their own.
SELECT e.emp_id, e.emp_name, d.dept_name AS emp_dept, p.project_name, pd.dept_name AS project_dept
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id
JOIN Projects p ON e.project_id = p.project_id
JOIN Departments pd ON p.dept_id = pd.dept_id
WHERE e.dept_id <> p.dept_id;

-- Q7. List all employees along with their manager’s name (self-join).
SELECT e.emp_id, e.emp_name, m.emp_name AS manager_name
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.emp_id;

-- Q8. Show the number of employees working in each department.
SELECT d.dept_name, COUNT(e.emp_id) AS num_employees
FROM Departments d
LEFT JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name;

-- Q9. Show the departments which do not have any employees.
SELECT d.dept_id, d.dept_name
FROM Departments d
LEFT JOIN Employees e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;

-- Q10. Generate all possible combinations of department and project names (cross join).
SELECT d.dept_name, p.project_name
FROM Departments d
CROSS JOIN Projects p;


-- Part B – Window Functions

-- Q1. For each employee’s sales, show the previous sale amount (using LAG).
SELECT emp_id, sale_id, sale_date, sale_amount,
       LAG(sale_amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS prev_sale
FROM Sales;

-- Q2. For each employee’s sales, show the next sale amount (using LEAD).
SELECT emp_id, sale_id, sale_date, sale_amount,
       LEAD(sale_amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS next_sale
FROM Sales;

-- Q3. Show the difference between each employee’s current sale and their previous sale.
SELECT emp_id, sale_id, sale_date, sale_amount,
       sale_amount - LAG(sale_amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS diff_from_prev
FROM Sales;

-- Q4. Assign a row number to each sale of every employee ordered by sale_date.
SELECT emp_id, sale_id, sale_date, sale_amount,
       ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY sale_date) AS row_num
FROM Sales;

-- Q5. Find the highest sale made by each employee using a window function (not GROUP BY).
SELECT emp_id, sale_id, sale_date, sale_amount,
       MAX(sale_amount) OVER (PARTITION BY emp_id) AS highest_sale
FROM Sales;

