-- create table student(
-- 	id int primary key auto_increment comment "学号",
-- 	name varchar(20) not null comment "姓名",
-- 	gender char(20) not null comment "性别",
-- 	age int comment "年龄",
-- 	class varchar(20) comment '所在班级',
-- 	phone varchar(20) comment '联系电话'
-- );

-- create table course(
-- 	id int primary key auto_increment comment "课程编号",
-- 	name varchar(30) not null comment "课程名称",
-- 	credit int comment "学分"
-- );

-- create table score(
-- 	id int primary key auto_increment ,
-- 	student_id int not null comment "学生id",
-- 	course_id int not null comment "课程id",
-- 	score decimal(4,1) comment "分数",
-- 	exam_date date comment "考试时间",
-- 	CONSTRAINT fk_score_student FOREIGN KEY (student_id) REFERENCES student(id) ON DELETE CASCADE,
--     CONSTRAINT fk_score_course FOREIGN KEY (course_id) REFERENCES course(id) ON DELETE CASCADE,
--     -- 唯一约束：一个学生同一门课只能有一条记录
--     CONSTRAINT uk_student_course UNIQUE (student_id, course_id)	
-- );

-- insert into student values 
-- (0,'赵雷', '男', 18, '高三(1)班', '13800001001'),
-- (0,'钱云', '女', 17, '高三(2)班', '13800001002'),
-- (0,'孙风', '男', 18, '高三(1)班', '13800001003'),
-- (0,'李雨', '女', 19, '高三(3)班', NULL),
-- (0,'周五', '男', 17, '高三(2)班', '13800001005');

-- insert into course values
-- (0,'数据结构', 4),
-- (0,'高等数学', 5),
-- (0,'大学英语', 3),
-- (0,'计算机原理', 4);

-- insert into score (student_id, course_id, score, exam_date) values
-- (1, 1, 85.5, '2026-06-10'),
-- (1, 2, 90.0, '2026-06-12'),
-- (1, 3, 78.0, '2026-06-15'),
-- (2, 1, 92.0, '2026-06-10'),
-- (2, 2, 88.5, '2026-06-12'),
-- (2, 4, 95.0, '2026-06-18'),
-- (3, 1, 60.0, '2026-06-10'),
-- (3, 2, 65.0, '2026-06-12'),
-- (3, 3, 72.5, '2026-06-15'),
-- (3, 4, 55.0, '2026-06-18'),
-- (4, 1, 50.0, '2026-06-10'),
-- (4, 3, 88.0, '2026-06-15'),
-- (4, 4, NULL, '2026-06-18'), -- 缺考
-- (5, 2, 82.0, '2026-06-12'),
-- (5, 3, 69.5, '2026-06-15');

-- insert into student values
-- (0,"吴杰","男",18,"高三(1)班","13800001006");

-- update  course set credit = 5 where name = "数据结构";

-- delete from student where id = 1;

-- select name,class from student where phone is  null;

-- select name from course where credit > 3;

-- select * from score where score < 60 order by score asc ;
 
-- select student_id , AVG(score) 平均分,MAX(score) 最高分,MIN(score) 最低分 from  score
-- group by student_id 
-- order by 平均分 desc;

-- select 
-- 	course_id , 
-- 	SUM(case when score >= 60 then 1 else 0 end) as 及格人数,
-- 	concat(round(sum(case when score >= 60 then 1 else 0 end) / count(*)*100,2),"%") as 及格率
-- 	from score
-- 	group by course_id;













