create database student;

show databases;

use student;

-- 1. table with constraints
create  table students (
student_id INT PRIMARY KEY,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20),
dob DATE NOT NULL,
gender CHAR(1) CHECK (gender IN('M','F'))
);

-- table without constraints
create table courses (
course_id INT,
course_name VARCHAR(100),
credits int
);

-- 2.adding constraints using alter
-- primary key on course_id
ALTER TABLE courses add constraint PRIMARY KEY (course_id); 

-- not null on course_name
ALTER TABLE courses MODIFY course_name VARCHAR(100) NOT NULL;

-- Check credits (must be between 1 and 6)
ALTER TABLE courses ADD constraint CHECK (credits between 1 and 6);

-- 3.create a relationship with foreign key
-- creating an enrollments table and adding foreign key constraints 

CREATE TABLE enrollments (
    enroll_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES students(student_id),
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- table with on delete cascade
CREATE TABLE enrollments_cascade(
		enroll_id INT PRIMARY KEY,
        student_id INT,
        course_id INT,
        CONSTRAINT fk_student_cas FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
		CONSTRAINT fk_course_cas FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- 4.add new coiumn email
ALTER TABLE students ADD email VARCHAR(100);

-- Rename column dob to date_of_birth
ALTER TABLE students RENAME COLUMN dob TO date_of_birth;
        
-- drop column creditis from courses

-- 5.drop vs truncate
-- insert a few rows into students and courses.

INSERT INTO students (student_id,first_name,last_name, date_of_birth, gender, email)
VALUES (1, 'aadya','reddy','2000-01-01','F', 'aadyareddy1@gmail.com'),
       (2, 'sudha' ,'varma','1999-02-03','F','sudha@gmail.com'),
       (3,'sudhanshu','sharma','1997-05-08','M','sudhanshu@gmail.com');

INSERT INTO courses (course_id, course_name)
VALUES (101, 'maths'),
       (102, 'chemistry'),
       (103,'Biology');
-- 

INSERT INTO enrollments (enroll_id, student_id, course_id)
VALUES (1,1,101),
       (2,2,102),
       (3,3,103);

-- TRUNCATE on enrollments(removes all rows, keeps table structure)
TRUNCATE TABLE enrollments;

ALTER TABLE enrollments DROP foreign key fk_course;

-- DROP removes table structure completely
DROP TABLE courses;




