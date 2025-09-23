-- MySQL Functions Assignment

-- Date & Time Functions

-- 1. Show current date, time, and timestamp separately.
SELECT CURDATE() AS current_date,
       CURTIME() AS current_time,
       NOW() AS current_timestamp;

-- 2. Display each employee’s hire year, month number, and month name.
SELECT emp_id, emp_name,
       YEAR(hire_date) AS hire_year,
       MONTH(hire_date) AS hire_month_num,
       MONTHNAME(hire_date) AS hire_month_name
FROM Employees;

-- 3. Find which quarter each employee was hired in.
SELECT emp_id, emp_name, QUARTER(hire_date) AS hire_quarter
FROM Employees;

-- 4. Display hire dates with their corresponding week numbers.
SELECT emp_id, emp_name, hire_date, WEEK(hire_date) AS week_num
FROM Employees;

-- 5. Show the 200th day of the year 2025 using MAKEDATE.
SELECT MAKEDATE(2025, 200) AS day_200;

-- 6. Create a time value '09:15:00' using MAKETIME.
SELECT MAKETIME(9, 15, 0) AS new_time;

-- 7. Find out the difference in time between '14:45:00' and '09:30:00'.
SELECT TIMEDIFF('14:45:00','09:30:00') AS time_difference;

-- 8. Convert '15/08/2025' into a proper date using STR_TO_DATE.
SELECT STR_TO_DATE('15/08/2025','%d/%m/%Y') AS proper_date;

-- 9. Show employee hire date and extract day, month, year separately.
SELECT emp_id, emp_name, hire_date,
       DAY(hire_date) AS day,
       MONTH(hire_date) AS month,
       YEAR(hire_date) AS year
FROM Employees;

-- 10. Find employees hired in the month of January.
SELECT emp_id, emp_name, hire_date
FROM Employees
WHERE MONTH(hire_date) = 1;



-- String Functions


-- 1. Concatenate first name and last name into one column.
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM Employees;

-- 2. Display first 3 characters of last name.
SELECT emp_name, LEFT(last_name, 3) AS first_3_chars FROM Employees;

-- 3. Show names in upper and lower case.
SELECT UPPER(emp_name) AS upper_name, LOWER(emp_name) AS lower_name FROM Employees;

-- 4. Find position of '@' in each email.
SELECT emp_name, LOCATE('@', email) AS at_position FROM Employees;

-- 5. Replace domain 'example.com' with 'company.org'.
SELECT REPLACE(email,'example.com','company.org') AS new_email FROM Employees;

-- 6. Reverse the first name of each employee.
SELECT emp_name, REVERSE(first_name) AS reversed_first FROM Employees;

-- 7. Show the length of each employee email.
SELECT emp_name, LENGTH(email) AS email_length FROM Employees;

-- 8. Trim spaces from ' SQL Practice '.
SELECT TRIM(' SQL Practice ') AS trimmed_string;

-- 9. Extract the last 4 characters from email addresses (domain).
SELECT RIGHT(email,4) AS last_4_chars FROM Employees;

-- 10. Display employees whose last name starts with 'S'.
SELECT emp_id, emp_name, last_name
FROM Employees
WHERE last_name LIKE 'S%';



-- Numeric Functions


-- 1. Show absolute value of -1000.
SELECT ABS(-1000) AS abs_value;

-- 2. Find the ceiling and floor values of 123.45.
SELECT CEIL(123.45) AS ceil_value, FLOOR(123.45) AS floor_value;

-- 3. Round the number 98.7654 to 2 decimals.
SELECT ROUND(98.7654,2) AS rounded_value;

-- 4. Show modulus when 55 is divided by 6.
SELECT MOD(55,6) AS modulus_value;

-- 5. Find square root of 121.
SELECT SQRT(121) AS sqrt_value;

-- 6. Raise 2 to the power of 8.
SELECT POW(2,8) AS power_value;

-- 7. Find natural log and base-10 log of 1000.
SELECT LN(1000) AS natural_log, LOG10(1000) AS log10_value;

-- 8. Display the sign of -45, 0, and 20.
SELECT SIGN(-45) AS sign_neg, SIGN(0) AS sign_zero, SIGN(20) AS sign_pos;

-- 9. Show 3 random numbers between 0 and 1.
SELECT RAND() AS rand1, RAND() AS rand2, RAND() AS rand3;

-- 10. Find highest and lowest salary from employees table.
SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary
FROM Employees;

-- 11. Display employee salary truncated to 2 decimals.
SELECT emp_id, emp_name, TRUNCATE(salary,2) AS truncated_salary
FROM Employees;

-- 12. Add a random bonus (between 500 and 2000) to each employee’s salary.
SELECT emp_id, emp_name, salary,
       salary + FLOOR(RAND()*(2000-500+1)+500) AS salary_with_bonus
FROM Employees;

