create database Company;
use company;
CREATE TABLE Employee(E_Name varchar(50) , Location varchar(20),
                       Age int , Dept Varchar(20), Gender Varchar(10));
desc employee;
select * from employee;
set sql_safe_updates=0
INSERT into employee values('Krishna' , 'Dwaraka' , 30 , 'Saviour' , 'M');

INSERT INTO employee values('Arjun' , 'Indraprast' , 25 ,'Fighter','M'),
                            ('Bheem' , 'Barsana' , 27 , 'Wrestler' , 'M');

ALTER table employee add column Marriage varchar(25); 
UPDATE  employee set marriage = 'single' where gender ='m';
UPDATE  employee set marriage = 'Married' where e_name='krishna';
ALTER table employee add column position varchar(25); 
UPDATE EMPLOYEE set position ='King' where e_name = 'krishna';
UPDATE employee set position ='General' where e_name='Arjun';
UPDATE employee set position ='Prince' where e_name='Bheem';
UPDATE EMPLOYEE set e_name ='Bheema' where position='prince';
SELECT @@SQL_SAFE_UPDATES;

drop table employee;