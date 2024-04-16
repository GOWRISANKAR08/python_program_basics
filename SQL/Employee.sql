CREATE DATABASE OFFICE;  -- CREATE A DATABASE FILE
USE OFFICE;     -- SELECTING FILE
CREATE TABLE EMPLOYEE (empid INT PRIMARY KEY, name VARCHAR(50),salary INT);  -- CREATE A TABLE AND ASSIGN 3 COLUMN
SELECT * FROM EMPLOYEE; -- view the file
INSERT INTO EMPLOYEE VALUES(100,'GOWRISANKAR',35000);
INSERT INTO EMPLOYEE (name,empid) VALUES('SAM',101);
INSERT INTO EMPLOYEE VALUES(108,'SANKAR',35000,"developer"),(106,"Mani",2555,"developer");
INSERT INTO EMPLOYEE VALUES(108,'SANKAR',35000,"developer");
						   
alter table employee add column (role varchar(100));
update employee set role = "soft dev",salary = 100000; -- update entier table
update employee set role = "Analyst" , salary = 150000 where empid =108; -- update specify row 
delete from employee where empid = 108 ; -- delete a specify row
alter table employee drop column role;
drop table if  exists employee ; -- deleteentier table



