
CREATE DATABASE IF NOT EXISTS employees;
USE employees;


CREATE TABLE departments (
    dept_no     INT PRIMARY KEY,
    dept_name   VARCHAR(100) NOT NULL UNIQUE,
    dept_location VARCHAR(50)
);



CREATE TABLE employees (
    emp_no      INT PRIMARY KEY,
    birth_date  DATE NOT NULL,
    first_name  VARCHAR(14) NOT NULL,
    last_name   VARCHAR(16) NOT NULL,
    gender      CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
    hire_date   DATE NOT NULL DEFAULT (CURRENT_DATE),
    emp_salary  DECIMAL(12,2) CHECK (emp_salary > 0),
    dept_no     INT,
    CONSTRAINT fk_dept FOREIGN KEY (dept_no)
        REFERENCES departments(dept_no)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


INSERT INTO departments (dept_no, dept_name, dept_location) 
VALUES (1, 'Human Resources', 'Bangalore'),
       (2, 'Finance', 'Mumbai'),
       (3, 'IT', 'Hyderabad');
 
describe departments;

INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date, emp_salary, dept_no)
VALUES (103, '1990-01-01', 'Arun', 'Vasa', 'M', '2020-05-01', 60000, 3),
       (104, '1992-03-10', 'Anita', 'Shah', 'F', '2021-06-01', 55000, 2);


INSERT INTO employees VALUES (103, '1991-07-15', 'John', 'Doe', 'M', '2022-08-01', 50000, 11);

-- 7) Query
SELECT * FROM employees;
SELECT * FROM departments;

DELETE FROM employees
WHERE emp_no = 103;

DELETE FROM employees
WHERE emp_no = 104;

-- 8) Example of cascade delete
DELETE FROM departments WHERE dept_no = 2;

-- 9) Schema modifications (demonstration)
-- Change salary column precision
ALTER TABLE employees MODIFY emp_salary DECIMAL(15,2);

-- Rename columns
ALTER TABLE departments CHANGE dept_location location VARCHAR(100);
ALTER TABLE employees CHANGE emp_salary salary DECIMAL(15,2);

-- 10) Rename tables
ALTER TABLE departments RENAME TO company_departments;
ALTER TABLE employees RENAME TO company_employees;

-- 11) Cleanup
TRUNCATE TABLE company_employees;  -- Clears all employee data
DROP TABLE company_employees;
DROP TABLE company_departments;
