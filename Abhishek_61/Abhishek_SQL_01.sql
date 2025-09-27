
-- create and inserting data
CREATE DATABASE company_db;
USE company_db;

CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    hire_date DATE,
    email VARCHAR(100),
    salary DECIMAL(10,2)
);


INSERT INTO employees (first_name, last_name, department, hire_date, email, salary) VALUES
('ABHISHEK', 'NAARYANADAS', 'IT', '2025-06-15', 'abhishek.narayanadas@example.com', 55000.00),
('Arun', 'Vasa', 'IT', '2021-06-15', 'arun.vasa@example.com', 55000.00),
('Priya', 'Sharma', 'HR', '2020-03-10', 'priya.sharma@example.com', 48000.00),
('Rahul', 'Patel', 'Finance', '2019-11-25', 'rahul.patel@example.com', 60000.00),
('Neha', 'Reddy', 'IT', '2022-01-05', 'neha.reddy@example.com', 53000.00),
('Kiran', 'Singh', 'Marketing', '2023-07-20', 'kiran.singh@example.com', 45000.00);

select * from employees;