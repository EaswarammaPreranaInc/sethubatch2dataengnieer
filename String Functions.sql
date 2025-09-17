-- String Functions
select * from employees;
 -- Concatenate first name and last name into one column
SELECT CONCAT(first_name ,last_name) AS full_name
FROM employees;

-- Display first 3 characters of last name. 
SELECT first_name, last_name, LEFT(last_name, 3) AS last_name_prefix
FROM employees;

-- Show names in upper and lower case.
 SELECT first_name, upper(first_name) as upper_case_name,Lower(first_name) AS lower_case_name
FROM employees;

-- Find position of '@' in each email 
SELECT emp_id, email, LOCATE('@', email) AS at_position
FROM employees;

--  Replace domain 'example.com' with 'company.org'.
SELECT first_name,email, REPLACE(email, 'example.com', 'company.org') AS updated_email
FROM employees;

-- Reverse the first name of each employee
SELECT first_name, REVERSE(first_name) AS reversed_name
FROM employees;

--   Show the length of each employee email.
select first_name, email, length(email)
from employees;

--  Trim spaces from ' SQL Practice '.
select TRIM('   SQL Practice   ') AS trimmed_text; 

--  Extract the last 4 characters from email addresses (domain)
SELECT first_name, email, right(email, 4) AS last_email_prefix
FROM employees;

--  Display employees whose last name starts with 'S'.
select * from employees
where last_name like 's%';