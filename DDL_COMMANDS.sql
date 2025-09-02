/* 
Assignment: DDL Commands – Student Database
Design a simple Student Database for a college. The database should store information about students, their courses, and enrollments.
*/

CREATE DATABASE IF NOT EXISTS Student;

USE Student;


/* 
Questions
Q1. CREATE Tables (with & without constraints)
*/

/* 
Create a table students with the following columns (add constraints where needed):
student_id (INT, Primary Key)
first_name (VARCHAR(50), NOT NULL)
last_name (VARCHAR(50))
dob (DATE, NOT NULL)
gender (CHAR(1), check constraint: only 'M' or 'F')
*/

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    dob DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F'))
);


/* 
Create another table courses without constraints with the following columns:
course_id (INT)
course_name (VARCHAR(100))
credits (INT)
*/

CREATE TABLE courses (
    course_id INT,
    course_name VARCHAR(100),
    credits INT
);


/* 
Q2. Add Constraints using ALTER
*/

/* 
Using ALTER TABLE, modify the courses table to add:
Primary key on course_id
*/

ALTER TABLE courses ADD PRIMARY KEY (course_id);


/* 
Using ALTER TABLE, modify the courses table to add:
NOT NULL on course_name
*/

ALTER TABLE courses MODIFY course_name VARCHAR(100) NOT NULL;


/* 
Using ALTER TABLE, modify the courses table to add:
Check constraint on credits (must be between 1 and 6)
*/

ALTER TABLE courses ADD CHECK (credits BETWEEN 1 AND 6);


/* 
Q3. Create a Relationship with Foreign Key
*/

/* 
Create an enrollments table with:
enroll_id (INT Primary Key)
student_id (INT)
course_id (INT)
Add foreign key constraints so that:
student_id references students(student_id)
course_id references courses(course_id)
Try creating this with and without ON DELETE CASCADE, and note the difference.
*/

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
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

/* 
Without ON DELETE CASCADE:  
If you try to delete a row from the parent table (students or courses) while related rows exist in the enrollments table, the database will block the deletion. 
This ensures data integrity and prevents accidental loss of related records. However, it also means you must manually remove the child rows in enrollments before you can delete the parent. 
This approach is safer and best suited when you want strict control over data deletion.

With ON DELETE CASCADE:  
When you delete a row from the parent table, the database will automatically remove all related rows in the enrollments table. 
This keeps data consistent without requiring manual cleanup. 
It is convenient, especially when child rows should not exist without their parent, but it can also be risky if deletions are not handled carefully since more data may be removed than intended.
*/


/* 
Q4. ALTER Commands Practice
Perform the following changes:
*/

/* 
Add a new column email (VARCHAR(100)) to the students table.
*/

ALTER TABLE students ADD COLUMN email VARCHAR(100);

/* 
Rename the column dob in students to date_of_birth.
*/

ALTER TABLE students CHANGE COLUMN dob date_of_birth DATE;

/* 
Drop the column credits from the courses table.
*/

ALTER TABLE courses DROP COLUMN credits;


/* 
Q5. DROP vs TRUNCATE
Insert a few rows into students and courses.
Use TRUNCATE on the enrollments table and observe the difference vs DELETE.
Finally, use DROP TABLE to remove the courses table completely.
*/

/* 
Insert a few rows into students and courses.
*/

INSERT INTO students (student_id, first_name, last_name, date_of_birth, gender, email)
VALUES
(1, 'Sai', 'Kumar', '2000-01-15', 'M', 'saikumar@example.com'),
(2, 'Kiran', 'Kirat', '1999-03-22', 'M', 'kirankirat@example.com'),
(3, 'Anjali', 'Sharma', '2001-07-05', 'F', 'anjalisharma@example.com'),
(4, 'Ravi', 'Teja', '1998-11-19', 'M', 'raviteja@example.com'),
(5, 'Meena', 'Reddy', '2000-09-30', 'F', 'meenareddy@example.com');


/* 
Use TRUNCATE on the enrollments table and observe the difference vs DELETE.
*/

INSERT INTO courses (course_id, course_name)
VALUES
(101, 'Database Systems'),
(102, 'Operating Systems'),
(103, 'Computer Networks'),
(104, 'Data Structures'),
(105, 'Python');

/* 
Finally, use DROP TABLE to remove the courses table completely.
*/

DELETE FROM enrollments;
/* DELETE removes rows but keeps table structure. 
   we can add WHERE conditions (e.g., DELETE FROM enrollments WHERE course_id=101). 
   DELETE can be rolled back if inside a transaction. 
*/

TRUNCATE TABLE enrollments;
/* TRUNCATE removes all rows instantly, resets auto-increment counters and cannot use WHERE conditions. 
   It is faster than DELETE and cannot usually be rolled back. 
*/


/* 
4. DROP removes the table entirely, along with its structure and data. 
*/
DROP TABLE courses;















