-- create table books (
--   id int primary key auto_increment,
--   title varchar(100) not null,
--   author varchar(50),
--   category varchar(30),
--   price decimal(10,2),
--   stock int default 0
-- );

-- insert into books (title,author,category,price,stock) values
-- ('三体', '刘慈欣', '科幻', 45.00, 10),
-- ('活着', '余华', '文学', 35.00, 5),
-- ('流浪地球', '刘慈欣', '科幻', 30.00, 0),
-- ('百年孤独', '马尔克斯', '外国文学', 55.00, 8),
-- ('小王子', '圣埃克苏佩里', '童话', 25.00, 15);

-- select title,author,price from books;
-- select * from books where category = '科幻';
-- select title,price from books where price >30 order by price desc;
-- insert into books (title,author,category,price,stock) values
-- ("白夜行","东野圭吾","推理",50.00,3);

-- update books set stock = 20 where title = '三体';
-- delete from books where stock = 0;
update books set price = price * 0.9 where author = '刘慈欣';


