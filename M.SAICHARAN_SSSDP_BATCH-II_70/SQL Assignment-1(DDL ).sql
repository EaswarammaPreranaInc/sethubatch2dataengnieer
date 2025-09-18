-- Assignment: DDL Commands – Student Database
-- Design a simple Student Database for a college. The database should store information about students, their courses, and enrollments.

-- Questions
-- Q1. CREATE Tables (with & without constraints)

-- Create a table students with the following columns (add constraints where needed):

-- student_id (INT, Primary Key) first_name (VARCHAR(50), NOT NULL)

-- last_name (VARCHAR(50) dob (DATE, NOT NULL)

-- gender (CHAR(1), check constraint: only 'M' or 'F')


-- Create another table courses without constraints with the following columns:

-- course_id (INT) course_name (VARCHAR(100)) credits (INT)



CREATE DATABASE IF NOT EXISTS students;

use students;

create table students (
  student_id  INT Primary Key,
  first_name  VARCHAR(50) NOT NULL,
  last_name   VARCHAR(50),
  dob         DATE NOT NULL,
  gender      CHAR(1), check(gender IN ('M' , 'F')));
 
 create table courses(
  course_id   INT,
  course_name VARCHAR(100),
  credits     INT
  );
  
-- Q2. Add Constraints using ALTER

-- Using ALTER TABLE, modify the courses table to add:

-- Primary key on course_id

-- NOT NULL on course_name

-- Check constraint on credits (must be between 1 and 6)


ALTER TABLE courses MODIFY course_id INT PRIMARY KEY;
  
  ALTER TABLE courses MODIFY course_name VARCHAR(100);
  
ALTER TABLE courses ADD constraint credits check (credits between 1 and 6);
 
  
  -- Q3. Create a Relationship with Foreign Key

-- Create an enrollments table with:

-- enroll_id (INT Primary Key)

-- student_id (INT)

-- course_id (INT)

-- Add foreign key constraints so that:

-- student_id references students(student_id)

-- course_id references courses(course_id)

-- Try creating this with and without ON DELETE CASCADE, and note the difference.


  CREATE TABLE enrollments (
    enroll_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
DROP TABLE enrollments;

 CREATE TABLE enrollments (
    enroll_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)ON DELETE CASCADE 
);


-- Q4. ALTER Commands Practice

-- Perform the following changes:

-- Add a new column email (VARCHAR(100)) to the students table.

-- Rename the column dob in students to date_of_birth.

-- Drop the column credits from the courses table.
 ALTER TABLE students ADD email VARCHAR(100);
 
 ALTER TABLE students change dob date_of_birth DATE NOT NULL;
 
 ALTER TABLE COURSES DROP COLUMN credits;
 
 -- Q5. DROP vs TRUNCATE

-- Insert a few rows into students and courses.

-- Use TRUNCATE on the enrollments table and observe the difference vs DELETE.

-- Finally, use DROP TABLE to remove the courses table completely.

INSERT INTO students (student_id, first_name, last_name, date_of_birth, gender, email) VALUES 
(1, 'sai', 'charan', '1998-08-25', 'M', 'saicharan@gmail.com'),
(2, 'rajesh', 'rajesh', '2002-10-02', 'M', 'rrajesh@gmail.com'),
(3, 'ram', 'babu', '1995-05-05', 'M', 'rramu@gmail.com');


INSERT INTO courses (course_id, course_name) VALUES 
(101, 'python'),
(102, 'Java'),
(103, 'C');


INSERT INTO enrollments (enroll_id, student_id, course_id) VALUES
(1, 1, 101),
(2, 2, 102),
(3, 3, 103);
          

TRUNCATE TABLE enrollments;


