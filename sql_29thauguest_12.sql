-- Table with constraints
CREATE database students;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    dob DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F'))
);
use students;
-- Table without constraints
CREATE TABLE courses (
    course_id INT,
    course_name VARCHAR(100),
    credits INT
);

Q2. Add Constraints using ALTER


-- Add Primary Key
ALTER TABLE courses
ADD CONSTRAINT pk_courses PRIMARY KEY (course_id);

-- Add NOT NULL
ALTER TABLE courses
MODIFY course_name VARCHAR(100) NOT NULL;

-- Add Check Constraint
ALTER TABLE courses
ADD CONSTRAINT chk_credits CHECK (credits BETWEEN 1 AND 6);


-- Add new column email
ALTER TABLE students
ADD email VARCHAR(100);

-- Rename dob to date_of_birth
ALTER TABLE students
RENAME COLUMN dob TO date_of_birth;

-- Drop column credits
ALTER TABLE courses
DROP COLUMN credits;
select * from courses;
select * from students;
-- Insert some rows
INSERT INTO students (student_id, first_name, last_name, date_of_birth, gender, email)
VALUES (1, 'Ravi', 'Kumar', '2000-05-12', 'M', 'ravi@example.com'),
       (2, 'Sita', 'Devi', '2001-08-20', 'F', 'sita@example.com');

INSERT INTO courses (course_id, course_name)
VALUES (101, 'Database Systems'),
       (102, 'Operating Systems');

-- TRUNCATE enrollments (removes all rows but keeps table structure)
TRUNCATE TABLE courses;

-- DELETE enrollments (can remove specific rows, logs more details)
DELETE FROM students WHERE student_id = 1;

-- DROP courses table (removes table completely)
DROP TABLE courses;