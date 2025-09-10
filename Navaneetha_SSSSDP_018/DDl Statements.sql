
CREATE DATABASE IF NOT EXISTS employees;

USE employees;

CREATE TABLE employees (
    emp_no      INT,
    birth_date  DATE,
    first_name  VARCHAR(14),
    last_name   VARCHAR(16),
    gender      CHAR(1),
    hire_date   DATE
);
drop table employees;

CREATE TABLE employees (
    emp_no      INT             NOT NULL ,
    birth_date  DATE            NOT NULL,
    first_name  VARCHAR(14)     NOT NULL,
    last_name   VARCHAR(16)     NOT NULL,
    gender      char(1)         NOT NULL,    
    hire_date   DATE            NOT NULL
);

CREATE TABLE employees (
    emp_no      INT             NOT NULL PRIMARY KEY,
    birth_date  DATE            NOT NULL,
    first_name  VARCHAR(14)     NOT NULL,
    last_name   VARCHAR(16)     NOT NULL,
    gender      CHAR(1)         NOT NULL,
    hire_date   DATE            NOT NULL
);

CREATE TABLE employees (
    emp_no      INT             NOT NULL PRIMARY KEY,
    birth_date  DATE            NOT NULL,
    first_name  VARCHAR(14)     NOT NULL,
    last_name   VARCHAR(16)     NOT NULL,
    gender      CHAR(1)         NOT NULL CHECK (gender IN ('M', 'F')),
    hire_date   DATE            NOT NULL
);

CREATE TABLE departments (
    dept_no     INT PRIMARY KEY,
    dept_name   VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE employees (
    emp_no      INT PRIMARY KEY,
    birth_date  DATE NOT NULL,
    first_name  VARCHAR(14) NOT NULL,
    last_name   VARCHAR(16) NOT NULL,
    gender      CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
    hire_date   DATE NOT NULL,
    dept_no     INT,
    CONSTRAINT fk_dept FOREIGN KEY (dept_no) REFERENCES departments(dept_no)
);

INSERT INTO departments (dept_no, dept_name) 
VALUES (1, 'Human Resources'), 
       (2, 'Finance'), 
       (3, 'IT');
       
 INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date, dept_no)
VALUES (101, '1990-01-01', 'Arun', 'Vasa', 'M', '2020-05-01', 3),
       (102, '1992-03-10', 'Anita', 'Shah', 'F', '2021-06-01', 2);      
       
INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date, dept_no)
VALUES (103, '1991-07-15', 'John', 'Doe', 'M', '2022-08-01', 11);       


select * from employees;
select * from departments
-- with and with out cascade
DELETE FROM departments WHERE dept_no = 2;

drop table employees;
drop table departments;

CREATE TABLE employees (
    emp_no      INT PRIMARY KEY,
    birth_date  DATE NOT NULL,
    first_name  VARCHAR(14) NOT NULL,
    last_name   VARCHAR(16) NOT NULL,
    gender      CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
    hire_date   DATE NOT NULL,
    dept_no     INT,
    CONSTRAINT fk_dept FOREIGN KEY (dept_no) 
        REFERENCES departments(dept_no)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

select * from employees;
select * from departments;

-- Add a new column to departments
ALTER TABLE departments ADD location VARCHAR(50);



-- Add a new column to employees
ALTER TABLE employees ADD salary DECIMAL(10,2);



-- Change dept_name size from 50 → 100
ALTER TABLE departments MODIFY dept_name VARCHAR(100);

-- Change salary from DECIMAL(10,2) → DECIMAL(12,2)
ALTER TABLE employees MODIFY salary DECIMAL(12,2);

-- Rename location → dept_location
ALTER TABLE departments CHANGE location dept_location VARCHAR(50);

-- Rename salary → emp_salary
ALTER TABLE employees CHANGE salary emp_salary DECIMAL(12,2);


-- Add UNIQUE constraint to dept_name
ALTER TABLE departments ADD CONSTRAINT unique_dept UNIQUE (dept_name);

-- Add CHECK constraint to ensure salary > 0
ALTER TABLE employees ADD CONSTRAINT chk_salary CHECK (emp_salary > 0);

-- Drop unique constraint
ALTER TABLE departments DROP INDEX unique_dept;

-- Drop check constraint
ALTER TABLE employees DROP CHECK chk_salary;

-- Remove emp_salary column
ALTER TABLE employees DROP COLUMN emp_salary;

-- add forigen key
ALTER TABLE employees 
ADD CONSTRAINT fk_dept FOREIGN KEY (dept_no) 
REFERENCES departments(dept_no)
ON DELETE CASCADE
ON UPDATE CASCADE;

-- drop forigen key
ALTER TABLE employees DROP FOREIGN KEY fk_dept;

-- Rename departments to company_departments
ALTER TABLE departments RENAME TO company_departments;

-- Rename employees to company_employees
ALTER TABLE employees RENAME TO company_employees;

-- Set default hire_date as today
ALTER TABLE employees ALTER hire_date SET DEFAULT (CURRENT_DATE);

-- Remove default
ALTER TABLE employees ALTER hire_date DROP DEFAULT;

-- Drop the employees table
DROP TABLE employees;

-- Drop the departments table
DROP TABLE departments;

-- Now truncate
TRUNCATE TABLE employees;