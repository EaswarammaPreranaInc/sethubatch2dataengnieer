-- Employees Table
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    project_id INT,
    manager_id INT
);

INSERT INTO Employees (emp_id, emp_name, dept_id, project_id, manager_id) VALUES
(1, 'Alice',   10, 100, NULL),
(2, 'Bob',     10, 101, 1),
(3, 'Charlie', 20, 100, 1),
(4, 'David',   30, 102, 2),
(5, 'Eve',     40, NULL, 3);

-- Departments Table
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO Departments (dept_id, dept_name, location) VALUES
(10, 'HR',        'New York'),
(20, 'Finance',   'London'),
(30, 'IT',        'New York'),
(50, 'Marketing', 'Chicago');

-- Projects Table
CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    dept_id INT,
    project_name VARCHAR(50)
);

INSERT INTO Projects (project_id, dept_id, project_name) VALUES
(100, 20, 'Budgeting'),
(101, 10, 'Recruitment'),
(102, 30, 'Migration'),
(103, 50, 'Campaign');