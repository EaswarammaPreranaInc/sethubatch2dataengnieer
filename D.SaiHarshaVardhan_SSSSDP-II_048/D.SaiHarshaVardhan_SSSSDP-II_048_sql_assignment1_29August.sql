CREATE DATABASE StudentDB;
use StudentDB;

create table students(
   student_id int primary key, 
   first_name varchar(50) not null,
   last_name varchar(50),
   dob date not null,
   gender char(1) check (gender in ('M' or 'F'))
);

create table courses(
    course_id int,
    course_name varchar(100),
    credits int
);

alter table courses
add primary key (course_id),
modify course_name varchar(100) not null;

alter table courses
add check (credits between 1 and 6);

create table enrollments(
    enroll_id  int primary key,
    student_id int,
    course_id int,
    foreign key (student_id) references students(student_id),
    foreign key (course_id) references courses(course_id)
);

alter table students 
add email varchar(100),
change dob date_of_birth date not null;

alter table courses
drop column credits;

alter table students
drop check students_chk_1;

alter table students
add check (gender in ('M', 'F'));

insert into students values(1, 'Harsha Vardhan', 'Dabbiru', '2003-03-14', 'M', 'har@gmail.com'),
						   (2, 'Ravi', 'Donkada', '2004-02-17', 'M', 'rav@gmail.com'),
                           (3, 'Siva', 'Kuda', '2003-04-17', 'M', 'siv@gmail.com'),
                           (4, 'Supraja', 'Majji', '2003-05-05', 'F', 'sup@gmail.com'),
                           (5, 'Veronica', 'Karthiko', '2004-08-07', 'F', 'ver@gmail.com');

insert into courses values(101, 'Data Engineer'),
						  (102, 'Full Stack Python'),
                          (103, 'SAP'),
                          (104, 'Networking'),
                          (105, 'Dotnet');
                          
truncate table enrollments;
drop table courses;



