-- date & time functions--

-- Show current date, time, and timestamp separately.
select current_date();
select current_time();
select current_timestamp();
select * from employees;

-- Display each employee’s hire year, month number, and month name. 
select
first_name, last_name, year(hire_date) as hire_year,
month(hire_date) as hire_month_number,
monthname(hire_date) as hire_month_name
from employees;

-- Find which quarter each employee was hired in.
SELECT first_name, hire_date, QUARTER(hire_date) AS hire_quarter
FROM employees;

-- Display hire dates with their corresponding week numbers. 
SELECT first_name, hire_date, WEEK(hire_date) AS hire_week
FROM employees;

-- Show the 200th day of the year 2025 using MAKEDATE. 
SELECT MAKEDATE(2025, 200) AS two_hundredth_day_2025;

-- Create a time value '09:15:00' using MAKETIME.
 SELECT MAKETIME(09, 15, 00) AS custom_time;
 
 -- Find out the difference in time between '14:45:00' and '09:30:00'.
 SELECT TIMEDIFF('14:45:00', '09:30:00') AS time_difference;
 
 -- Convert '15/08/2025' into a proper date using STR_TO_DATE.
 SELECT STR_TO_DATE('15-08-2025', '%d-%m-%Y') AS formatted_date;

 -- Show employee hire date and extract day, month, year separately.
 --  YEAR() : Extract year from hire_date
SELECT first_name, hire_date, DAYNAME(hire_date) AS hire_day_name, YEAR(hire_date) AS hire_year,  MONTH(hire_date) AS hire_month
FROM employees;

 -- Find employees hired in the month of January.
 SELECT first_name, hire_date, MONTHNAME(hire_date) AS hire_month_name
FROM employees
where MONTHNAME(hire_date)='january';