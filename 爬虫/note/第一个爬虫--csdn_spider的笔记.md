# 对第一个爬虫csdn_spider.py的笔记

---

[toc]

## 0.一些说明

该爬虫对csdn论坛中的大部分内容进行爬取



## 1.文件位置

```
../practice/spider/csdn-spider/csdn-spider.py
```



## 2.动态加载的判断

现在浏览器的f12查看当前网页的Elements，找到目标的属性，复制，

然后再网页中右键查看网页源码

ctrl+f判断复制内容是否在网页源码中,没有即动态加载

csdn论坛左侧目录即js动态加载的

(之所以是左侧目录为了遍历，需要获取其url)



## 3.找到csdn论坛左侧目录的文件

通过在网页源码中定位到一个left_menu的东西确定是这个文件。

```
https://bbs.csdn.net/dynamic_js/left_menu.js?csdn
```

但是查看里面都是Unicode,于是用一下网页工具翻译查看

[Unicode转中文](http://www.bejson.com/convert/unicode_chinese/)



## 4.从相对路径到绝对路径

法一：判断是否http开头然后选择是否加

法二：（推荐）

```
# parse中的urljoin实现的也是相同效果，如果已经存在域名则不会再添加
from  urllib import parse

domain = "https://bbs.csdn.net/"
all_last_url.append(parse.urljoin(domain,item))
```



## 5.创建model

### 找到primary_key

一般在个人网页最后面的一串数字或者字符串就是唯一的，可以作为primary_key

### 数据处理

尽可能将字符串类型变数字类型，如年月日可以变成date类型，以方便后续查找等操作。





## 6.xpath的相对路径下的绝对路径

当xpath路径表达式有多个匹配时候，xpath选择器选出来的是selector组成的列表，我们可以对列表中的每一个元素继续进行xpath查找。

**但是，需要注意的是，如果没有加 . ，则会将路径表达式拼接，返回的是拼接后在原html中查找的结果**

```
res_text=requests.get(topic_url).text
sel=Selector(text=res_text)
body_sel=sel.xpath("//tbody/tr")
topic=Topic()  # 记录数据
for tr in body_sel:
    state_text_list=tr.xpath(".//td[1]/span/text()").extract()  #这里加了.
    # 上面如果没有加. 则变为sel.xpath("//tbody/tr//td[1]/span/text()")在sel中查找的结果，这样可能会有偏差。
    topic.state=state_text_list[0]
```





## 7.时间日期的数据类型转换

将str转化为datetime类型

```
from datetime import datetime
date_string = '2020-02-09 18:29'

date_time = datetime.strptime(date_string,"%Y-%m-%d %H:%M")
```



## 8.爬取数据后要做的事情

1. 对数据不存在的保险措施
2. 确定数据类型正确



## 9.翻页遍历

查找下一页的标签来进行遍历，好处是不用知道有多少页



## 10.对主键自己设置的数据库的存储

```
# 如果自己设置了主键，则要save(force_insert=True)，否则它只会作更新操作
# 但是要注意如果主键已经存在就会报错，所以还要检查主键是否存在来决定是否用force_insert=True


# 所以进行判断
exist_topic=Topic.select().where(Topic.id==topic.id)
if exist_topic:
	topic.save()
else:
	topic.save(force_insert=True)
```



## 11.回车换行符的处理

用`.strip()`方法即可去掉



## 12.UA

csdn个人主页要加UA才能爬取

```
 headers={ 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36' }

res_text = requests.get(url,headers=headers).text
```



## 13.提取小技巧

当一系列东西要连续提取，而且他们标签相同，那么可以先提取相同标签的值，生成值列表，然后将值一个一个给到对应的





## 语法转换问题

### 将一个列表形式的字符串转为真正的list

```
 import ast
 a_list_str="['apple','banana','orange']"
 # 转换
 a_list = ast.literal_eval(a_list_str)
```

