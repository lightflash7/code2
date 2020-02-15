import re
from bs4 import BeautifulSoup

http_txt = """<html>
    <!-- 网页的标题、图标... -->
    <head>
        <mate charset="utf-8">
        <title>第一个网页</title>
    </head>
    <!-- 网页的具体内容 -->
    <body>
        这是网页的内容
        <a href="http://www.baidu.com" target="_blank">百度</a>

        <h>这里是h1内容</h>
        <h>666666666</h>
        <h>666666666</h>
        <h>666666666</h>
        <h>666666666</h>

        <p>ppppppppppp</p>

    <div>
        <p>ppppppppppp</p>
    </div>

        <ul>
            <li>hahaha</li>
            <li>hahaha</li>
            <li>hahaha</li>
        </ul>

        <ol>
            <li>ahahah</li>
            <li>ahahah</li>
            <li>ahahah</li>
        </ol>

    <img src="text.png">
    </body>
</html>"""


bs = BeautifulSoup(http_txt,"html.parser")
# re_txt=re.compile(r"b..y")
# aim_tag=bs.find_all(re_txt)
#
# children = aim_tag[0].children
# for child in children:
#     print(child.name)



aim_txt=bs.find("a")
# print(aim_txt.get("href"))
print(aim_txt["href"])