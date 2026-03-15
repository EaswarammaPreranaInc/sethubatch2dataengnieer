use students;
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    dob DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F'))
);
desc students;
INSERT INTO students(student_id,first_name,last_name,dob,gender) 
values (48,'Sai','lakshman','2003-11-05','M'),(50,'Sai','Seeta','2004-10-08','F'),(78,'Sai','krishna','2013-11-06','M')
 select * from students;

CREATE TABLE courses (
    course_id INT(3) PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL,
	credits INT (3) 
);

desc courses;
INSERT INTO courses(course_id,course_name,credits) 
values (134,'Web Technologies','3'),(501,'Software engineering','4'),(978,'Programming with python','3')
select * from courses

ALTER TABLE courses
MODIFY COLUMN course_name VARCHAR(255) NOT NULL;

ALTER TABLE courses
ADD CONSTRAINT chk_credits CHECK (credits BETWEEN 1 AND 6);

CREATE TABLE enrollments (
  enroll_id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
); 
select * from enrollments;
 DROP TABLE enrollments;

CREATE TABLE enrollments (
  enroll_id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);
desc enrollments;
INSERT INTO enrollments(enroll_id,student_id,course_id) 
values (13344,50,978),(52031,78,501),(12978,48,134);

INSERT INTO students (student_id, first_name, dob)
VALUES
  (5, 'Alice', '2003-05-21'),
  (7, 'Bob', '2002-10-10'),
  (9, 'Charlie', '2004-02-12');
  
INSERT INTO courses (course_id, course_name)
VALUES
  (101, 'Physics'),
  (102, 'Mathematics'),
  (103, 'Biology');
truncate table enrollments;
select * from enrollments;
DROP TABLE enrollments

