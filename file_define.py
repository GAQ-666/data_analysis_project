"""
和文件相关的类定义
"""

#  导入事先定义好的数据定义类
from data_define import Record
import json
#  先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
class FileReader:
    def read_data(self) -> list[Record]:    #  用类型注解说明返回值
        """读取文件的数据，读到的每一条数据都转换为Record对象，将他们都封装进List内返回即可"""
        pass

#  开始做具体的实现（定义两个子类）
class TextFileReader(FileReader):           #  文本数据的文件读取器

    def __init__(self,path):
        self.path = path                    #  定义成员变量，记录文件路径

    #  复写（实现抽象方法）父类方法，实现多态
    def read_data(self) -> list[Record]:    #  list[Record]用来标记返回的是列表
        with open(self.path,"r",encoding="utf-8") as f: #  读取文件

            record_list = []
            lines = f.readlines()
            for line in lines[1:]:                      #  在for循环内完成文件数据的提取
                line = line.strip()
                data_list = line.split(',')
                #  构建Record类对象
                record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
                # print(record)
                record_list.append(record)              #  把数据追加进提前定义好的record空列表
        return record_list                              #  返回追加好的列表


class JsonFileReader(FileReader):               #  json数据的文件读取器

    def __init__(self,path):
        self.path = path                        #  定义成员变量记录文件的路径

    def read_data(self) -> list[Record]:        #  依旧复写（实现抽象方法）父类方法
        with open(self.path,"r",encoding="utf-8") as f:
            data_list = json.loads(f.read())

            record_list = []
            for data_dict in data_list:
                record = Record(data_dict["date"],data_dict["id"],int(data_dict["sales"]),data_dict["province"])
                record_list.append(record)
        return record_list

#  以下为通用分析方法
def analyze_data(reader:FileReader) -> None:
    #  统一调用read_data()（不管是txt还是json）
    record_list = reader.read_data()
    #  统一做数据分析（比如求总销售额）
    total = 0
    for record in record_list:
        total += record.sales

    print(f"共读取到{len(record_list)}条数据")
    print(f"总销售额:{total}元")

#  以下为测试阶段
if __name__ == '__main__':
    text_file_reader = TextFileReader("D:/2011年1月全国销售数据.txt")
    text_file_reader.read_data()
    # for record in text_file_reader.read_data():
        # print(record)
    json_file_reader = JsonFileReader("D:/2011年2月全国销售数据.txt")
    # for record in json_file_reader.read_data():
    #     print(record)
    print(json_file_reader.read_data())
    # analyze_data(text_file_reader)
    # analyze_data(json_file_reader)