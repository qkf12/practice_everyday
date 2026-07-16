-- 创建一个表 名叫b name是一列字符类型是varchar 长度是10  
-- height是一列 数据类型是decimal 总共五位数 保留两位有效数字  1.23等
-- create table b(
--   name varchar(10),
--   height decimal(5,2)
-- );

-- 创建c表  第一列 是id 数据类型是 int 第二列是name 数据类型是varchar 长度是20
-- 第三列是age 数据类型是tinyint unsigned （无符号小正数）
-- create table c(
--   id int,
--   name varchar(20),
--   age tinyint unsigned
-- );

-- err是错误的意思  不是标红

-- 在表c中插入数据  
-- insert into c values(1,'李老大',28);


-- 输入两个数据 指定字段插入
-- insert into c (id,name) values (2,'曹操');
-- insert into c (id,age) values (3,60);

-- 一次性输入多个值
-- insert into c values (4,'关羽',40),
-- (5,'刘备',60),
-- (6,'赵云',50);

insert into c (id,name) values (7,'孟德尔'),
(8,'关云长'),
(9,'雍正');


