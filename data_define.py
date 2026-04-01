"""
数据定义的类
"""

class Record:

    """定义一个构造方法方便接收数据"""
    def __init__(self,date,id,sales,province):
        self.date = date
        self.id = id
        self.sales = sales
        self.province = province

    #  定义一个魔术方法（美化打印输出）
    def __str__(self):
        return f"{self.date},{self.id},{self.sales},{self.province}"
    def __repr__(self):
        return f"{self.date},{self.id},{self.sales},{self.province}"