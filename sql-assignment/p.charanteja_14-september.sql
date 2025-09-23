--  CURRENT_DATE : Returns today's date
SELECT CURRENT_DATE();

--  CURRENT_TIME : Returns current system time

-- time and date functions

SELECT CURRENT_TIME();

--  CURRENT_TIMESTAMP : Returns current date and time
SELECT CURRENT_TIMESTAMP();

--  DATE() : Extract only the DATE part from a datetime value
-- Example with NOW()
SELECT NOW() AS full_datetime, DATE(NOW()) AS only_date;

--  DATE_ADD() : Add interval to a date
SELECT first_name, hire_date, DATE_ADD(hire_date, INTERVAL 2 MONTH) AS plus_2_months
FROM employees;

--  ADDDATE() : Same as DATE_ADD()
SELECT first_name, hire_date, ADDDATE(hire_date, INTERVAL 15 DAY) AS plus_15_days
FROM employees;

--  ADDTIME() : Add hours/minutes/seconds to a datetime or time
SELECT NOW() AS current_time3, ADDTIME(NOW(), '02:30:00') AS after_2hr30min;

--  DATEDIFF() : Difference between two dates (in days)
SELECT first_name, DATEDIFF(DATE_ADD(CURDATE(), INTERVAL 2 MONTH), hire_date) AS days_in_company
FROM employees;

--  DAY() : Returns the day number of the month
SELECT first_name, hire_date, DAY(hire_date) AS hire_day_number
FROM employees;

--  DAYNAME() : Returns weekday name
SELECT first_name, hire_date, DAYNAME(hire_date) AS hire_day_name
FROM employees;


--  NOW() : Returns current date and time
SELECT NOW();

--  HOUR() : Extract hour from a datetime
SELECT NOW() AS full_time, HOUR(NOW()) AS current_hour;

--  MINUTE() : Extract minutes from a datetime
SELECT NOW() AS full_time, MINUTE(NOW()) AS current_minute;

--  SECOND() : Extract seconds from a datetime
SELECT NOW() AS full_time, SECOND(NOW()) AS current_second;

--  YEAR() : Extract year from hire_date
SELECT first_name, hire_date, YEAR(hire_date) AS hire_year
FROM employees;

--  MONTH() : Extract month number from hire_date
SELECT first_name, hire_date, MONTH(hire_date) AS hire_month
FROM employees;

--  MONTHNAME() : Extract month name from hire_date
SELECT first_name, hire_date, MONTHNAME(hire_date) AS hire_month_name
FROM employees
where MONTHNAME(hire_date)='June';

--  QUARTER() : Extract quarter (1–4) from hire_date
SELECT first_name, hire_date, QUARTER(hire_date) AS hire_quarter
FROM employees;

--  WEEK() : Week number of the year
SELECT first_name, hire_date, WEEK(hire_date) AS hire_week
FROM employees;

--  MAKEDATE(year, day_of_year) : Create a date
SELECT MAKEDATE(2025, 100) AS hundredth_day_2025; -- Returns 2025-04-10

--  MAKETIME(hour, minute, second) : Create a time
SELECT MAKETIME(12, 45, 30) AS custom_time; -- Returns 12:45:30

--  TIME() : Extract only the time part from a datetime
SELECT NOW() AS full_datetime, TIME(NOW()) AS only_time;

--  TIMEDIFF() : Difference between two time/datetime values
SELECT TIMEDIFF('2025-09-12 12:00:00', '2025-09-13 10:30:00') AS time_difference;

-- STR_TO_DATE() : Convert string into a date
SELECT STR_TO_DATE('12-09-2025', '%d-%m-%Y') AS formatted_date;




-- string functions

-- Concatenate first and last name
SELECT CONCAT(first_name, ' +', last_name) AS full_name
FROM employees;

-- FIND_IN_SET(str, strlist) : Finds position of a string in a comma-separated list
SELECT FIND_IN_SET('IT', 'HR,Finance,IT,Marketing') AS position;

--  INSTR(str, substr) : Returns position of substring
SELECT email, INSTR(email, 'e') AS at_position
FROM employees;

--  LCASE(str) or LOWER(str) : Convert to lowercase
SELECT first_name, LCASE(first_name) AS lower_case_name
FROM employees;

-- LEFT(str, n) : Returns leftmost n characters
SELECT last_name, LEFT(last_name, 1) AS short_last_name
FROM employees;

--  LENGTH(str) : Returns length in bytes
SELECT first_name, LENGTH(first_name) AS name_length
FROM employees;

--  LOWER(str) : Same as LCASE()
SELECT LOWER(last_name) AS lower_name
FROM employees;

--  LTRIM(str) : Removes leading spaces
SELECT LTRIM('    SQL Training  ') AS trimmed_text;
 
-- REPEAT(str, n) : Repeats string n times
SELECT REPEAT('Hi ', 3) AS repeated_text;

--  REPLACE(str, from_str, to_str) : Replace substring
SELECT email, REPLACE(email, 'example.com', 'company.org') AS updated_email
FROM employees;

--  REVERSE(str) : Reverse string
SELECT first_name, REVERSE(first_name) AS reversed_name
FROM employees;

--  RIGHT(str, n) : Returns rightmost n characters
SELECT email, RIGHT(email, 10) AS domain
FROM employees;

--  RTRIM(str) : Removes trailing spaces
SELECT RTRIM('MySQL Basics     ') AS trimmed_text;

--  SPACE(n) : Returns string of n spaces
SELECT CONCAT('Hello', SPACE(5), 'World') AS spaced_text;

--  SUBSTR(str, pos, len) or SUBSTRING(str, pos, len)
SELECT first_name, SUBSTR(first_name, 2, 3) AS mid_name_part
FROM employees;

--  SUBSTRING_INDEX(str, delim, count)
-- Returns part of string before/after delimiter
SELECT email,
       SUBSTRING_INDEX(email, '@', 1) AS username,
       SUBSTRING_INDEX(email, '@', -1) AS domain
FROM employees;

--  TRIM(str) : Removes both leading and trailing spaces
SELECT TRIM('   SQL Functions   ') AS trimmed_text;

--  UPPER(str) : Converts to uppercase
SELECT first_name, UPPER(first_name) AS upper_case_name
FROM employees;



-- numeric functions

--  CEIL(x) / CEILING(x) : Smallest integer >= x
SELECT CEIL(45.2) AS ceil_value; -- 46

--  FLOOR(x) : Largest integer <= x
SELECT FLOOR(45.8) AS floor_value; -- 45

--  EXP(x) : Exponential (e^x)
SELECT EXP(2) AS exponential; -- e^2

--  LOG(x) : Natural logarithm
SELECT LOG(10) AS natural_log;

SELECT LN(10) AS natural_log;

SELECT LOG(2,10) AS log10base2;


--  LOG10(x) : Base-10 logarithm
SELECT LOG10(1000) AS log_base10; -- 3

--  ROUND(x, d) : Round number to d decimals
SELECT ROUND(123.4467, 1) AS rounded_value; -- 123.46

--  TRUNCATE(x, d) : Truncate number to d decimals
SELECT TRUNCATE(123.4567, 3) AS truncated_value; -- 123.45

--  MOD(x, y) : Modulus (remainder)
SELECT MOD(17, 4) AS modulus; -- 1

--  POWER(x, y) or POW(x, y) : x raised to power y
SELECT POWER(3, 4) AS power_value; -- 81

--  SQRT(x) : Square root
SELECT SQRT(49) AS square_root; -- 7

--  ABS(x) : Absolute value
SELECT -50 AS number, ABS(-50) AS absolute_value;


--  SIGN(x) : Returns -1, 0, or 1 depending on sign
SELECT SIGN(-25), SIGN(0), SIGN(100);

--  RAND() : Random number between 0 and 1
SELECT round(RAND()*100,0) AS random_number;

--  PI() : Value of π
SELECT PI();

--  GREATEST(x, y, ...) : Largest value
SELECT GREATEST(10, 45, 32, 67, 5) AS greatest_value;

--  LEAST(x, y, ...) : Smallest value
SELECT LEAST(10, 45, 32, 67, 5) AS least_value;

