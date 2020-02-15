from peewee import *
from datetime import date

# 对mysql数据库用MySQLDATAbase函数
db = MySQLDatabase('spider', host="127.0.0.1", port=3306, user="root", password="1145071624")


class BaseModel(Model):
    class Meta:
        database = db


"""
char类型要注意设置最大长度
对于无法确定最大长度的字段，可以设置问题text，数据库中text不限长度
要尽量将数据格式化处理，将字符串类型尽可能变为数字类型，比如年月日变为date类型
要注意设置default的值和null是否为True
"""



# 记录每篇文章数据，
class Topic(BaseModel):
    state=CharField()           # 结贴状态
    score=IntegerField(default=0)  #赏分
    title=CharField(max_length=1000) #文章名字
    authod = CharField()   #发起者名字
    reply_num = IntegerField(default=0)  #回复数量
    read_num =IntegerField(default=0) # 阅读数量
    last_modify_time=DateField()   # 最后更改时间
    id = IntegerField(primary_key=True)  # 文章的id，在文章url最后一个字段
    jtl= FloatField(default=0)       # 发起者的结贴率
    praise_num=IntegerField(default=0)  # 点赞数量
    content=TextField(default="") # 内容


# 记录每篇文章回复数据
class Answer(BaseModel):
    passage_id = IntegerField()  # 文章id
    message_id=IntegerField(primary_key=True) #回答的id
    writer_name=CharField() # 回复者名字
    content=TextField(default='')  #回复内容
    praise_num=IntegerField(default=0)  #回复被点赞数
    answer_time = DateField() #回复时间


# 记录作者的具体数据
class Authod(BaseModel):
    name = CharField()    # 名称
    id=CharField(primary_key=True)  #网页最后面一个字段
    description = CharField(default='')  #个人描述
    boke_num= IntegerField(default=0)  #博客数量
    ziyuan_num=IntegerField(default=0) #资源数量
    luntan_num=IntegerField(default=0) #论坛数量
    Blink_num=IntegerField(default=0)  #Blink数量
    wenda_num=IntegerField(default=0)  #问答数量
    shoucang_num=IntegerField(default=0) #收藏数量
    zhuanlan_num=IntegerField(default=0) #专栏数量
    fans_num=IntegerField(default=0)  # 粉丝数量
    follow_num=IntegerField(default=0) # 关注数量
    paiming=IntegerField(default=0)  #排名










if __name__ == '__main__':
    # db.connect()                      # 创建连接
    db.create_tables([Topic,Answer,Authod])        # 创建表，传入一个列表数据类型，可以同时创建多个表
    # db.close()                        # 断开连接




