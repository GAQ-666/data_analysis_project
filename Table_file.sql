-- 河南省电商销售模拟数据

-- 先建一个库
create database if not exists ecommerce;

use ecommerce;
-- 河南地市表
drop table if exists city;
create table city (
			city_id int primary key,
			city_name varchar(100),
			region varchar(100) 
                  );
select * from city; 
-- 河南电商销售表
drop table if exists sales;
create table sales (
			id int primary key auto_increment,
            city_id int,
            sale_date date,			-- 2025年1 - 12月
            category varchar(100),	-- 品类: 实物/服务/跨境
            gmv decimal(12,2),		-- 交易额（万元）
            order_count int,		-- 订单数
            user_count int,			-- 购买用户数
            foreign key (city_id) references city (city_id)
            );						

-- 插入数据
insert into city (city_id,city_name,region) values 
(1,'郑州','豫中'),
(2,'洛阳','豫西'),
(3,'南阳','豫南'),
(4,'许昌','豫中'),
(5,'周口','豫东'),
(6,'商丘','豫东'),
(7,'驻马店','豫南'),
(8,'信阳','豫南'),
(9,'新乡','豫北'),
(10,'平顶山','豫中'),
(11,'开封','豫东'),
(12,'安阳','豫北'),
(13,'漯河','豫中'),
(14,'濮阳','豫北'),
(15,'三门峡','豫西'),
(16,'鹤壁','豫北'),
(17,'济源','豫西'),
(18,'永城','豫东');
select * from city;

-- 2025年1月实物类
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
values 
(1,'2025-01-01','实物',125000,250000,85000),
(2,'2025-01-01','实物',68000,135000,42000),
(3,'2025-01-01','实物',42000,85000,28000),
(4,'2025-01-01','实物',38000,78000,25000),
(5,'2025-01-01','实物',35000,72000,23000),
(6,'2025-01-01','实物',32000,66000,21000),
(7,'2025-01-01','实物',30000,62000,20000),
(8,'2025-01-01','实物',28000,58000,18000),
(9,'2025-01-01','实物',26000,54000,17000),
(10,'2025-01-01','实物',24000,50000,16000),
(11,'2025-01-01','实物',22000,46000,15000),
(12,'2025-01-01','实物',21000,44000,14000),
(13,'2025-01-01','实物',19000,40000,13000),
(14,'2025-01-01','实物',18000,38000,12000),
(15,'2025-01-01','实物',16000,34000,11000),
(16,'2025-01-01','实物',15000,32000,10000),
(17,'2025-01-01','实物',14000,30000,9500),
(18,'2025-01-01','实物',13000,28000,9000);

-- 2025年1月服务类
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
values 
(1,'2025-01-01','服务',45000,180000,65000),
(2,'2025-01-01','服务',22000,88000,32000),
(3,'2025-01-01','服务',15000,60000,22000),
(4,'2025-01-01','服务',13000,52000,20000),
(5,'2025-01-01','服务',12000,48000,19000),
(6,'2025-01-01','服务',11000,44000,18000),
(7,'2025-01-01','服务',10000,40000,17000),
(8,'2025-01-01','服务',9500,38000,16000),
(9,'2025-01-01','服务',9000,36000,15000),
(10,'2025-01-01','服务',8500,34000,14000),
(11,'2025-01-01','服务',8000,32000,13000),
(12,'2025-01-01','服务',7500,30000,12000),
(13,'2025-01-01','服务',7000,28000,11000),
(14,'2025-01-01','服务',6500,26000,10000),
(15,'2025-01-01','服务',6000,24000,9500),
(16,'2025-01-01','服务',5500,22000,9000),
(17,'2025-01-01','服务',5000,20000,8500),
(18,'2025-01-01','服务',4500,18000,8000);

-- 2025年1月跨境电商
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
values 
(1,'2025-01-01','跨境',32000,95000,32000),
(2,'2025-01-01','跨境',15000,45000,15000),
(3,'2025-01-01','跨境',8000,24000,8000),
(4,'2025-01-01','跨境',7000,21000,7000),
(5,'2025-01-01','跨境',6000,18000,6000),
(6,'2025-01-01','跨境',5500,16500,5500),
(7,'2025-01-01','跨境',5000,15000,5000),
(8,'2025-01-01','跨境',4500,13500,4500),
(9,'2025-01-01','跨境',4000,12000,4000),
(10,'2025-01-01','跨境',3800,11400,3800),
(11,'2025-01-01','跨境',3500,10500,3500),
(12,'2025-01-01','跨境',3200,9600,3200),
(13,'2025-01-01','跨境',3000,9000,3000),
(14,'2025-01-01','跨境',2800,8400,2800),
(15,'2025-01-01','跨境',2500,7500,2500),
(16,'2025-01-01','跨境',2200,6600,2200),
(17,'2025-01-01','跨境',2000,6000,2000),
(18,'2025-01-01','跨境',1800,5400,1800);

+
drop table sales;
delete from sales limit 9999;-- where sale_date = '2025-03-01' limit 999;
-- 二月
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
select city_id,'2025-02-01',category,gmv*1.08,order_count*1.08,user_count
*1.08 from sales where sale_date = '2025-01-01';

-- 三月
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
select city_id,'2025-03-01',category,gmv*1.08,order_count*1.08,user_count
*1.08 from sales where sale_date = '2025-02-01';

-- 四月
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
select city_id,'2025-04-01',category,gmv*1.08,order_count*1.08,user_count
*1.08 from sales where sale_date = '2025-03-01';

-- 五月
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
select city_id,'2025-05-01',category,gmv*1.08,order_count*1.08,user_count
*1.08 from sales where sale_date = '2025-04-01';

-- 六月
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
select city_id,'2025-06-01',category,gmv*1.08,order_count*1.08,user_count
*1.08 from sales where sale_date = '2025-05-01';

-- 七月
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
select city_id,'2025-07-01',category,gmv*1.08,order_count*1.08,user_count
*1.08 from sales where sale_date = '2025-06-01';

-- 八月
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
select city_id,'2025-08-01',category,gmv*1.08,order_count*1.08,user_count
*1.08 from sales where sale_date = '2025-07-01';

-- 九月
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
select city_id,'2025-09-01',category,gmv*1.08,order_count*1.08,user_count
*1.08 from sales where sale_date = '2025-08-01';

-- 十月
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
select city_id,'2025-10-01',category,gmv*1.08,order_count*1.08,user_count
*1.08 from sales where sale_date = '2025-09-01';

-- 十一月
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
select city_id,'2025-11-01',category,gmv*1.08,order_count*1.08,user_count
*1.08 from sales where sale_date = '2025-10-01';

-- 十二月
insert into sales (city_id,sale_date,category,gmv,order_count,user_count)
select city_id,'2025-12-01',category,gmv*1.08,order_count*1.08,user_count
*1.08 from sales where sale_date = '2025-11-01';

