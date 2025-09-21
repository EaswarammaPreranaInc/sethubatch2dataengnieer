CREATE DATABASE employees_db;

USE employees_db;

CREATE TABLE departments (
dept_no INT PRIMARY KEY,
dept_name VARCHAR(50) NOT NULL UNIQUE);

CREATE TABLE employees (
emp_no INT PRIMARY KEY,
birth_date DATE NOT NULL,
first_name VARCHAR(14) NOT NULL,
last_name VARCHAR(16) NOT NULL,
gender CHAR(1) NOT NULL CHECK (gender IN ('M','F')),
hire_date DATE NOT NULL,
dept_no INT,
email VARCHAR(100) UNIQUE,
salary DECIMAL(10,2),
CONSTRAINT fk_dept FOREIGN KEY (dept_no) REFERENCES departments(dept_no)
);


INSERT INTO departments (dept_no, dept_name) VALUES
(1, 'HR'),
(2, 'Finance'),
(3, 'IT'),
(4, 'Sales');


INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date, dept_no, email, salary) VALUES
(101, '1997-06-15', 'Aarav', 'Mehta', 'M', '2020-01-10', 1, 'aarav.mehta@example.com', 55000.75),
(102, '1995-09-22', 'Ananya', 'Reddy', 'F', '2019-03-05', 2, 'ananya.reddy@example.com', 72000.50),
(103, '1998-12-11', 'Rohan', 'Mishra', 'M', '2018-07-19', 3, 'rohan.mishra@example.com', 68000.00),
(104, '1997-04-08', 'Radya', 'Iyer', 'F', '2021-06-01', 4, 'Radya.iyer@example.com', 48000.20),
(105, '1992-02-25', 'Devansh', 'Dixit', 'M', '2017-11-23', 3, 'devansh.dixit@example.com', 89000.90);

-- 1.concatenate first name and last name into one column
SELECT CONCAT(first_name,' ',last_name) As Name FROM employees;

-- 2.Display first 3 characters of last name
SELECT LEFT(last_name,3) AS LastName FROM employees;

-- 3. show names in upper and lower case 
SELECT UPPER(first_name) AS UpperName,
LOWER(first_name) AS LowerName from employees;

-- 4.find position of '@' in each email
SELECT email, INSTR(email, '@') AS at_position
FROM employees;

-- 5. replace domain 'example.com' with 'company.org'
SELECT email, 
REPLACE(email,'example.com','company.org') AS Email 
from employees;


-- 6.reverse the first name of each employee
SELECT first_name, REVERSE(first_name) As reversed_First_name FROM employees;

-- 7.show the length of each emoloyee eamail
SELECT first_name, LENGTH(first_name) AS first_name_length FROM employees;

-- 8.Trim spaces from 'SQL Practice'
SELECT TRIM('  SQL PRACTICE  ') AS trimmed_text;

-- 9.Extract the last 4 characters from email addresses(domain)
SELECT email, RIGHT(email,4) AS Last_char from employees;

-- 10.Display employees whose last name starts with 'S'
SELECT last_name from employees where last_name like 'S%';








