#  先导入所有的包
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import *

#  读取文件
with open("D:/GDP统计.txt","r",encoding="utf-8") as f:
    #  先接收列表，把所有行存进变量
    data_lines = f.readlines()
    #  在调用pop,从列表中删除0号元素
    data_lines.pop(0)
#  先定义一个空字典对象,准备将数据传入为字典存储
data_dict = {}

#  用for循环遍历取出数据
for line in data_lines:
    #  split功能将大列表分成许多个小列表,每个小列表的格式为[1960(年份),"国家",GDP数据]
    year = int(line.split(",")[0])   #  年份
    country = line.split(",")[1]     #  国家
    GDP = float(line.split(",")[2])  #  GDP数据
#  开始往字典里添加数据
#  因为字典没有append方法,所以以下方法行不通
    # dict1 = {year:[country,GDP]}
    # data_dict = data_dict.append(dict1)

#  可以用捕获异常并处理的方法添加
    try:
        #  先尝试往字典的year这个key里添加数据
        data_dict[year].append([country,GDP])
        #  如果没有进行到下一项
    except KeyError:
        #  当字典中不存在某项key时,令它等于一个value,会自动创建一个key
        data_dict[year]=[]
        #  在空列表中追加数据
        data_dict[year].append([country,GDP])
print(data_dict)
#  添加时间线
timeline = Timeline({"theme": ThemeType.CHALK})

#  从字典中取出数据用于构建图表
#  使用for循环构建图表,每一次循环就构建一个,通过时间线将他们连起来
for year in sorted(data_dict.keys()):                      #  sorted(字典.keys())是为了防止乱序,旧版本的for循环会乱序
    year_data_old = data_dict[year]
    #  将year_data里的数据按照从大到小排序
    year_data_old.sort(key=lambda x: x[1],reverse=True)    #  默认从小到大,reverse表示反转,sort()不需要重新赋值,返回值None
    print(year_data_old)                                   #  sorted()返回一个新的排序后的列表,需要赋值
    #  取出本年份前8位国家的数据
    year_data = year_data_old[0:8]
    #  先构建两份数轴空列表，准备传入数据
    x_data = []
    y_data = []
    #  需要再嵌套一层循环用来遍历内层列表,从而将每一份数据都追加到数据轴
    for country_GDP in year_data:
        x_data.append(country_GDP[0])                #  x轴添加国家
        y_data.append(country_GDP[1]/100000000)      #  y轴添加GDP数据,以亿为单位所以除以一亿
    #  数据已经追加完毕,不需要再进入内层for循环
    print(x_data)
    print(y_data)
    #  构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)",
                  y_data,label_opts=LabelOpts(position="right"),
                  itemstyle_opts=ItemStyleOpts(color="#14e0ff")
                  )
    #  反转x轴和y轴
    bar.reversal_axis()
    #  设置每年的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title = f"{year}年全球GDP排行")
    )
    timeline.add(bar,str(year))               #  str(year)表示时间线上的点的名字,将year转成了字符串
#  for循环每一年的数据,基于每一年的数据,创建每一年的bar对象
#  在for循环中,将每一年的bar对象添加到时间线

#  设置时间线自动播放
timeline.add_schema(
    play_interval=500,           #  自动播放设置的时间间隔,单位毫秒
    is_timeline_show=True,        #  是否在自动播放时显示时间线
    is_auto_play=True,            #  是否自动播放
    is_loop_play=False             #  是否连续自动播放
)
#  绘图
timeline.render("1960-2021年GDP排行.html")