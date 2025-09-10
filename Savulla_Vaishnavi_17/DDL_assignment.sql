
CREATE DATABASE IF NOT EXISTS students;

USE students;


CREATE TABLE student_info (
Roll_no              INT          Primary Key,

first_name           VARCHAR(50)  ,

last_name            VARCHAR(50),

dob                   DATE NOT NULL,

gender               CHAR(1)         NOT NULL CHECK (gender IN ('M', 'F'))
);

CREATE TABLE course (
course_id  INT,

course_name VARCHAR(100),

credits INT

);


-- Primary key on course_id
-- Change couse_id  to primary key
ALTER TABLE course MODIFY course_id INT PRIMARY KEY;

-- Change couse_name  to VARCHAR(100) NOT NULL
ALTER TABLE course MODIFY course_name VARCHAR(100) NOT NULL;

-- Check constraint on credits (must be between 1 and 6)
ALTER TABLE course ADD CONSTRAINT credits_num CHECK (credits BETWEEN 1 AND 6);

CREATE TABLE enrollments  (

    enroll_id      INT PRIMARY KEY,
    student_id     INT,
    CONSTRAINT fk_enroll1 FOREIGN KEY (Roll_no) REFERENCES student_info(Roll_no),
    course_id     INT,
    CONSTRAINT fk_enroll2 FOREIGN KEY (course_id) REFERENCES course(course_id)
);

-- Add a new column email (VARCHAR(100)) to the students table.
ALTER TABLE student_info ADD email VARCHAR(100);

-- Rename the column dob in students to date_of_birth.
ALTER TABLE student_info CHANGE dob date_of_birth VARCHAR(50);

-- Drop the column credits from the courses table.
ALTER TABLE course DROP credits;

select * from course;

-- Insert a few rows into students and courses.
INSERT INTO student_info (Roll_no ,first_name ,last_name,date_of_birth,gender)
VALUES (1,'John', 'Doe', '2022-08-01', 'M'),
(2, 'Anita', 'Shah',  '2021-06-01', 'F'),
(5,'AAA','BBB','2023-09-23','M');

INSERT INTO course (course_id,course_name)
values (102,'Maths'),
(104,'BIO');

-- Use TRUNCATE on the enrollments table and observe the difference vs DELETE.

-- Finally, use DROP TABLE to remove the courses table completely.
DROP TABLE course;








