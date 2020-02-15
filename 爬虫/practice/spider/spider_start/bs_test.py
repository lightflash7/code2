import re
from bs4 import BeautifulSoup

http_text = """<html>
	<head>
	<title>Build A Web Server</title>
	</head>
	<body>
	Hello World
	<div id="info-955">
		a text in div
	</div>
	</body>
</html>"""

# bs库的查找方法示例
bs = BeautifulSoup(http_text, "html.parser")
# div_tag = bs.find("div")
# div_tag = bs.find(id="info-955")
# div_tag=bs.find("div",id="info-955")
# div_tag= bs.find("div",id=re.compile(r"info-\d+"))
# div_tag=bs.find(string="text")
div_tag = bs.find_all("div")
for div in div_tag:
    print(div_tag.string)
