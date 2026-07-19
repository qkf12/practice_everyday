-- create table employees(
--   id int primary key auto_increment,
--   name varchar(50) not null,
--   phone varchar(20) unique,
--   dept varchar(30) default '待分配',
--   salary decimal (10,2)
-- );

-- insert into employees values(0,'张三','138001','技术部',8000),
-- (0,'李四','138002','市场部',6500),
-- (0,'王五',null ,'行政部',5000),
-- (0,'赵六','138003',default ,7000);

-- select * from employees;
-- select name,dept from employees where salary>6000;
-- select name,salary from employees order  by salary desc ;

-- update employees set dept = '研发中心' where name = '张三';
-- update employees set salary = salary * 1.1 where dept = '研发中心';
-- delete from employees where salary < 5500;

-- truncate table employees;
-- drop table employees;






