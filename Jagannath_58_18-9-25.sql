use company_db;
select * from employees;

-- Functions Assignment --
-- date function --
-- 1 Show current date, time, and timestamp separately.--
select current_date();
select current_time();
select current_timestamp();

 -- 2 Display each employee’s hire year, month number, and month name. --
 select first_name,year(hire_date),month(hire_date),monthname(hire_date) from employees;
 
--  3 Find which quarter each employee was hired in. --
select first_name,quarter(hire_date) as hired_quarter from employees;

 -- 4 Display hire dates with their corresponding week numbers. --
 select first_name,week(hire_date) from employees;
 
 -- 5 Show the 200th day of the year 2025 using MAKEDATE. --
 select makedate(2025,200) as two_hundredth_day;
 
 -- 6 Create a time value '09:15:00' using MAKETIME. --
 select maketime(09,15,00) as time;
 
 -- 7 Find out the difference in time between '14:45:00' and '09:30:00'. --
 select timediff('14:45:00','09:30:00') as time_diff;
 
 -- 8 Convert '15/08/2025' into a proper date using STR_TO_DATE. --
 select str_to_date('15-08-25','%d-%m-%y') as formatted_date;
 
 -- 9 Show employee hire date and extract day, month, year separately. --
select hire_date,day(hire_date) as hire_day from employees;
select hire_date,month(hire_date) as hire_month from employees;
select hire_date,year(hire_date) as hire_year from employees;

--  10 Find employees hired in the month of January. --
 select first_name,hire_date from employees where monthname(hire_date)='january';
 
 
 -- String function  --
 --  1 Concatenate first name and last name into one column. --
 select concat(first_name,'+',last_name) as full_name from employees;
 
 -- 2 Display first 3 characters of last name. --
 select last_name,left(last_name,3) as first_three from employees;
 
 -- 3 Show names in upper and lower case.--
 select first_name,upper(first_name) as upper_case from employees;
 select last_name,upper(last_name) as upper_case from employees;
 select first_name,lower(first_name) as lower_case from employees;
 select last_name,lower(last_name) as lower_case from employees;
 
--  4 Find position of '@' in each email. --
select email,locate('@',email) as position_of_at from employees;

 -- 5 Replace domain 'example.com' with 'company.org'. --
 SELECT email, REPLACE(email, 'example.com', 'company.org') AS updated_email FROM employees;
 
--  6 Reverse the first name of each employee. --
SELECT first_name, REVERSE(first_name) AS reversed_name FROM employees;

 -- 7 Show the length of each employee email. --
 select email,length(email) as email_length from employees;
 
 -- 8 Trim spaces from ' SQL Practice '. --
 select TRIM('   SQL Practice   ') as trimmed_text;
 
 -- 9 Extract the last 4 characters from email addresses (domain). --
 select right(email,4) as domain from employees;
 
 -- 10 Display employees whose last name starts with 'S' --
 select * from employees where last_name like 'S%'; 
 
 -- Numeric function --
 --  1 Show absolute value of -1000. --
 select -1000 as number, abs(-1000) as absolute_value;
 
 -- 2 Find the ceiling and floor values of 123.45. --
 select ceil(123.45) as ceil_value;
 select floor(123.45) as floor_value;
 
 -- 3 Round the number 98.7654 to 2 decimals. --
 select round(98.7654,2) as round_value;
 
 -- 4 Show modulus when 55 is divided by 6. --
 select mod(55,6) as modulus;
 
 -- 5 Find square root of 121. --
 select sqrt(121) as squre_root;
 
 -- 6 Raise 2 to the power of 8. --
 select pow(2,8) as power_value;
 
 -- 7 Find natural log and base-10 log of 1000. --
 select log10(1000) as log_base10;
 
-- 8 Display the sign of -45, 0, and 20. --
select SIGN(-45), SIGN(0), SIGN(20);

 -- 9 Show 3 random numbers between 0 and 1. --
 select rand() as random_number union all select rand() union all select rand();

 -- 10 Find highest and lowest salary from employees table. --
 select max(salary) as highest_salary,min(salary) as lowest_salary from employees;
 
 -- 11 Display employee salary truncated to 2 decimals. --
 select truncate(salary,2) as truncated_value from employees;
 
 -- 12 Add a random bonus (between 500 and 2000) to each employee’s salary --
 select emp_id,salary,salary + (500 + FLOOR(RAND() * 1501)) as salary_with_bonus from employees;
