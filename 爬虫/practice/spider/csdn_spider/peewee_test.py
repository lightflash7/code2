from peewee import *
from datetime import date

# 对mysql数据库用MySQLDATAbase函数
db = MySQLDatabase('spider', host="127.0.0.1", port=3306, user="root", password="1145071624")


class Person(Model):
    name = CharField()                # 数据及类型
    birthday = DateField()

    class Meta:
        database = db
        table_name = 'first_table'    # 表名


if __name__ == '__main__':
    db.connect()                      # 创建连接
    # db.create_tables([Person])        # 创建表，传入一个列表数据类型，可以同时创建多个表
    # db.close()                        # 断开连接


# 数据的增，删，改，查


# 数据的增  以Person类方式存储
#     uncle_bob = Person(name="xiaoming",birthday=date(1999,4,26))
#     uncle_bob.save()  # bob is now stored in the database
# 如果自己设置了主键，则要save(force_insert=True)，否则它只会作更新操作
# 但是要注意如果主键已经存在就会报错，所以还要检查主键是否存在来决定是否用force_insert=True





# 数据的查询（两种方法）   返回Person类     只取出一条数据   不分大小写
# 当数据不存在时用get方法会抛异常，所以最好用第一种且把get（）分开用，形成第三种获得所有数据的用法
    # grandma = Person.select().where(Person.name == 'bob').get()
    # grandma = Person.get(Person.name == 'bob')

    #下面这种查询方法得到一个ModelSelect类型数据，可以当成list来处理,且该方法不会抛异常
    # grandma = Person.select().where(Person.name == 'Bob')
    # for Person in grandma:
    #     print(Person.name, Person.birthday)


# 数据的修改，当我们查询到数据时，对数据的属性进行修改，然后再调用.save()方法即可完成对数据的修改。
#     grandma = Person.select().where(Person.name == 'Bob')
#     for Person in grandma:
#         Person.birthday=date(2020,2,14)
#         Person.save()


# 数据的删除：在查询到数据后调用类的.delete_instance()方法
    #注意：即使在这里创建的Person对象中没有id属性,但是数据库中有，一样可以通过id操作
    grandma = Person.select().where(Person.id == '7')
    for Person in grandma:
        Person.delete_instance()



