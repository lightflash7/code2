# 本爬虫爬取csdn论坛中的大部分内容，具体爬取内容看model
# 1. 判断左侧目录是否动态加载，这里找到是，且目录来源https://bbs.csdn.net/dynamic_js/left_menu.js?csdn

import requests
from scrapy import Selector
import re
import ast
from  urllib import parse
from csdn_spider.Model import *
from datetime import datetime


all_left_menu_url = []  # 左侧菜单
domain = "https://bbs.csdn.net/"





# 获取左侧菜单的内容，返回结果是个list
def get_left_menu_list():
    url = 'https://bbs.csdn.net/dynamic_js/left_menu.js?csdn'
    res_text = requests.get(url=url).text
    left_menu_list_str = re.search(r"forumNodes: (.*\])",res_text).group(1)
    if left_menu_list_str:
        # 要将里面的null变为json的none,不然下面转换会抛异常
        left_menu_list_str = left_menu_list_str.replace("null","None")
        # 将str转换为真list
        left_menu_list = ast.literal_eval(left_menu_list_str)
        return left_menu_list
    else:
        return []

# 获取列表中的url
def get_url(left_menu_list):
    # 找出所有没有children的url
    for item in left_menu_list:
       if "children" in item:
            get_url(item["children"])
       else:
            if "url" in item:
                all_left_menu_url.append(item["url"])


# 得到最后待解决和已解决的页面的url,即所有url
def get_last_url(all_left_menu_url):
    all_last_url = []  # 最终爬取的所有页面
    for item in all_left_menu_url:
        all_last_url.append(parse.urljoin(domain,item))
        all_last_url.append(parse.urljoin(domain,item+'/recommend'))
        all_last_url.append(parse.urljoin(domain,item+'/closed'))
    return  all_last_url


# 爬取last_url中的页面（非个人主页），是博客左列表中的页面
def get_topic_data(topic_url):
    res_text=requests.get(topic_url).text
    sel=Selector(text=res_text)
    body_sel=sel.xpath("//tbody/tr")
    for tr in body_sel:
        topic = Topic()  # 记录数据
        state_text_list=tr.xpath(".//td[1]/span/text()").extract()
        topic.state=state_text_list[0]
        score=tr.xpath(".//td[2]/em/text()").extract()
        if score:
            topic.score=int(score[0])
        title=tr.xpath(".//td[3]/a[starts-with(@href,'/topics')]/text()").extract()
        deeper_relative_url=tr.xpath(".//td[3]/a[starts-with(@href,'/topics')]/@href").extract()[0]
        topic.title=title[0]
        topic.id = int(deeper_relative_url.split('/')[-1])
        authod=tr.xpath(".//td[4]/a/text()").extract()
        topic.authod=authod[0]
        authod_homepage_relative_url=tr.xpath(".//td[4]/a/@href").extract()[0]
        nums=tr.xpath(".//td[5]/span/text()").extract()
        if nums:
            topic.reply_num=int(nums[0].split('/')[0])
            topic.read_num = int(nums[0].split('/')[1])
        last_modify_time=tr.xpath(".//td[6]/em/text()").extract()
        topic.last_modify_time=datetime.strptime(last_modify_time[0],"%Y-%m-%d %H:%M")

        # 对数据进行保存
        exist_topic=Topic.select().where(Topic.id==topic.id)
        if exist_topic:
            topic.save()
        else:
            topic.save(force_insert=True)

        # 对内部网页数据的提取
        deeper_page_url=parse.urljoin(domain,deeper_relative_url)
        get_article_data(deeper_page_url)

        # 对个人主页数据提取
        authod_homepage_url=parse.urljoin(domain,authod_homepage_relative_url)
        get_homepage_data(authod_homepage_url)


    # 爬取完一页的内容爬取下一页的内容，通过下一页标签的链接找到下一页的链接继续调用此方法
    # 要注意来自上一页的干扰，两者标签一样
    next_page_url=''
    next_page_sel=sel.xpath("//a[@class='pageliststy next_page']")
    for next_sel in  next_page_sel:
        if "下" in next_sel.xpath("./text()").extract()[0]:
            next_page_url=next_sel.xpath("./@href").extract()[0]
            next_page_url = parse.urljoin(domain, next_page_url)
            break
    if next_page_url:
        get_topic_data(next_page_url)





# 获取论坛内部数据页面数据，包括文章内容，结贴率，点赞数
def get_article_data(url):
    res_text = requests.get(url).text
    sel = Selector(text=res_text)
    div_sel = sel.xpath("//div[starts-with(@id,'post-')]")

    # 为了防止翻页后？page的干扰用正则表达式提取出来数字
    url_str = url.split('/')[-1]
    id_str = re.search("\d+", url_str).group(0)
    # 如果是第二页，两者不等，此时才是获取帖子发起内容和结贴率等的时候，并且评论从第二个div开始
    if id_str == url_str:
        start_point = 1
        # 先爬取topic中的文字内容，结贴率，点赞数等数据，在第一个id为post开头的div中
        authod_div =div_sel[0]
        topic=Topic()
        jtl=authod_div.xpath(".//div[@class='close_topic']/text()").extract()
        if jtl:
            jtl_text=jtl[0]
            topic.jtl = float(re.search("(\d.*)%",jtl_text ).group(1))
        praise_num=authod_div.xpath(".//label[@class='red_praise digg']//em/text()").extract()
        if praise_num:
            topic.praise_num=int(praise_num[0])
        content=authod_div.xpath(".//div[@class='post_body post_body_min_h']/text()|.//div[contains(@style,'text-')]/text()").extract()
        content=''.join(content).strip()
        if content:
            topic.content=content

        topic.id=int(id_str)
        exist_topic = Topic.select().where(Topic.id == topic.id)
        if exist_topic:
            topic.save()
    else:
        start_point = 0

    # 爬取answer中的数据
    for div in div_sel[start_point:]:
        answer=Answer()
        answer.passage_id=int(id_str)
        message_id_str=div.xpath("./@id").extract()[0]
        message_id=int(re.search("\d+",message_id_str).group(0))
        answer.message_id=message_id
        name=div.xpath(".//div[@class='nick_name']/a/text()").extract()[0]
        answer.writer_name=name
        time=div.xpath(".//label[@class='date_time']/text()").extract()[0]
        answer.answer_time=datetime.strptime(time,"%Y-%m-%d %H:%M:%S")
        praise_num=div.xpath(".//label[@class='red_praise digg']//em/text()").extract()
        if praise_num:
            answer.praise_num=int(praise_num[0])
        content = div.xpath(".//div[@class='post_body post_body_min_h']/text()|.//div[contains(@style,'text-')]/text()").extract()
        content = ''.join(content).strip()
        if content:
            answer.content = content
        # 对数据进行保存
        exist_answer=Answer.select().where(Answer.message_id==answer.message_id)
        if exist_answer:
            answer.save()
        else:
            answer.save(force_insert=True)

    # 爬取完一页的内容爬取下一页的内容，通过下一页标签的链接找到下一页的链接继续调用此方法
    # 要注意来自上一页的干扰，两者标签一样
    next_page_url = ''
    next_page_sel = sel.xpath("//a[@class='pageliststy next_page']")
    for next_sel in next_page_sel:
        if "下" in next_sel.xpath("./text()").extract()[0]:
            next_page_url = next_sel.xpath("./@href").extract()[0]
            next_page_url = parse.urljoin(domain, next_page_url)
            break
    if next_page_url:
        get_article_data(next_page_url)


# 获得主页数据
def get_homepage_data(url):
    authod=Authod()
    headers={ 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36' }
    res_text = requests.get(url,headers=headers).text
    sel = Selector(text=res_text)
    name_list=sel.xpath("//p[@class='lt_title']/text()").extract()
    name_str="".join(name_list).strip()
    authod.name=name_str

    authod.id=url.split('/')[-1]

    description=sel.xpath("//div[@class='description clearfix']/p/text()").extract()
    if description:
        authod.description=description[0].strip()

    li_sel=sel.xpath("//div[@class='me_chanel_bar clearfix']//li")
    num_list=[]
    for li in li_sel:
        span_str=li.xpath(".//span[@class]/text()").extract()
        if span_str:
            num_list.append(int(span_str[0].strip()))
        else:
            num_list.append(0)
    authod.boke_num=num_list[0]
    authod.ziyuan_num=num_list[1]
    authod.luntan_num=num_list[2]
    authod.Blink_num=num_list[3]
    authod.wenda_num=num_list[4]
    authod.shoucang_num=num_list[5]
    authod.zhuanlan_num=num_list[6]

    fans=sel.xpath("//div[@class='fans']//span/text()").extract()
    if fans:
        fans_num_str = re.search("\d+[kw]*", fans[0]).group(0)
        fans_num=num_decode(fans_num_str)
        authod.fans_num=fans_num
    follows=sel.xpath("//div[@class='att']//span/text()").extract()
    if follows:
        follows_num_str = re.search("\d+[kw]*", follows[0]).group(0)
        follows_num=num_decode(follows_num_str)
        authod.follow_num=follows_num

    paiming = sel.xpath("//div[@class='me_chanel_det_item access'][2]//span/text()").extract()
    if paiming:
        paiming_num_str = re.search("\d+[kw]*", paiming[0]).group(0)
        paiming_num = num_decode(paiming_num_str)
        authod.paiming = paiming_num

    exist_authod = Authod.select().where(Authod.id == authod.id)
    if exist_authod:
        authod.save()
    else:
        authod.save(force_insert=True)









def num_decode(nums_str):
    if nums_str.endswith('k'):
        num = int(nums_str[:-1]) * 1000
    elif nums_str.endswith('w'):
        num = int(nums_str[:-1]) * 10000
    else:
        num = int(nums_str)
    return num











if __name__ == '__main__':
    left_menu_list=get_left_menu_list()
    get_url(left_menu_list)
    all_last_url=get_last_url(all_left_menu_url)
    # print(all_last_url)
    # print(len(all_last_url))
    for url in all_last_url:
        get_topic_data(url)
        print("一个区论坛信息采集完成")
    print("论坛信息采集完成")
