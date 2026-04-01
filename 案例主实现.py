"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤:
1．设计一个类，可以完成数据的封装
2．设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3．读取文件，生产数据对象
4．进行数据需求的逻辑计算（计算每一天的销售额）
5．通过PyEcharts进行图形绘制
"""
from pyecharts.globals import ThemeType

#  导入提前定义好的读取文件用的包
from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pyecharts.charts import *
from pyecharts.options import *


#  直接传入文件的路径
text_file_reader = TextFileReader("D:/2011年1月全国销售数据.txt")
json_file_reader = JsonFileReader("D:/2011年2月全国销售数据.txt")

jan_data: list[Record] = text_file_reader.read_data()          #  jan表示1月
feb_data: list[Record] = json_file_reader.read_data()          #  feb表示2月，用两个变量来接收读取后的文件

#  将两个月份的数据合并为1个list来存储
all_data = jan_data + feb_data
# from pymysql import *
#
# #  链接数据库
# conn = Connection(
#     host="localhost",       #  主机名（ip）
#     port=3306,              #  端口
#     user="root",            #  账户
#     password="gaoyin789",   #  密码
#     autocommit=True,        #  自动提交更改事务，设置之后更改表内数据无需手动确认提交
# )

# #  先获取游标对象
# cursor = conn.cursor()
# #  创建一个数据库py_sql
# cursor.execute("create database if not exists py_sql charset utf8")
# #  select_db选择使用数据库
# conn.select_db("py_sql")
# #  创建一个表用来接收数据
# cursor.execute("""
#                 create table if not exists orders(
#                 order_date date ,
#                 order_id varchar(100) ,
#                 money float,
# #                 province varchar(100))
# #                 """)
# #  给已经存在的表加唯一性约束
# # cursor.execute("alter table orders add unique key (order_id)")
#
# #  组织sql语句将数据插入进新建的表中
# for record in all_data:
#     sql = f"insert ignore into orders(order_date,order_id,money,province) " \
#           f"values('{record.date}','{record.id}',{record.sales},'{record.province}')"
#
#     cursor.execute(sql)         #  执行sql语句成功将数据插入进了orders表中
#

#  关闭数据库
# conn.close()
#  开始进行数据计算
data_dict = {}                                                  #  定义一个空子典接收数据
for record in all_data :
    if record.date  in data_dict.keys() :
        # 字典中已存在此日期，将这次循环得到的record.sales与字典中的record.sales相加
        # data_dict[record.rate]表示取出字典中此日期的record.sales（销售额）
        data_dict[record.date] += record.sales
    else:
        #  字典中不存在此日期，构建一组键对值（record.rate: record.sales），把销售额记录进去
        data_dict[record.date] = record.sales
print(data_dict)

#  可视化图表开发
bar = Bar(init_opts=InitOpts(theme= ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))                                                               #  添加x轴的数据
bar.add_yaxis("销售额", list(data_dict.values()),label_opts=LabelOpts(is_show=False))     #  添加y轴的数据
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
#  构建图表
bar.render("每日销售额柱状图.html")