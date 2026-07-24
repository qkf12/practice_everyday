-- create table orders (
--   id int primary key auto_increment,
--   customer_name  varchar(20) not null,
--   product  varchar(30),
--   category  varchar(20),
--   price  decimal(10,2),
--   quantity  int,
--   order_date  date,
--   phone  varchar(20)  
-- );

-- insert into orders (customer_name, product, category, price, quantity, order_date, phone) values
--  ('张三', '苹果手机', '数码', 5999.00, 1, '2026-07-01', '138001'),
--  ('李四', '篮球鞋'  , '运动', 899.00 , 2, '2026-07-02', '138002'),
--  ('王五', '电饭煲'  , '家电', 499.00 , 1, '2026-07-03', NULL),        -- 电话为空
--  ('赵六', '华为手环', '数码', 299.00 , 3, '2026-07-04', '138004'),
--  ('张三', '跑步鞋'  , '运动', 599.00 , 1, '2026-07-05', '138001'),    -- 张三复购
--  ('孙七', '吸尘器'  , '家电', 899.00 , 1, '2026-07-06', '138006'),
--  ('周八', '智能音箱', '数码', 399.00 , 2, '2026-07-07', NULL),      -- 电话为空
--  ('李四', '移动电源', '数码', 199.00 , 1, '2026-07-08', '138002');
--  


-- drop table orders ;

-- select distinct customer_name from orders; 

-- select customer_name 顾客,price * quantity 总价 from orders;

-- select  * from orders where price >= 500;

-- select * from orders where category = "数码" and quantity > 1;

-- select  *  from orders where product  like "%手机%" or product  like "%手环%"

-- select product, price from orders where price  between 300 and 800;

-- select * from orders where category in ("数码","运动");

-- select customer_name,product from orders where phone is null ;

select customer_name 姓名,product 商品名,price * quantity 总价 from orders order by 总价 desc;






