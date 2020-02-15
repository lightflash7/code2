# 可以采用lxml库，这里我们用scrapy中的selector类（是一个对lxml的封装）
from scrapy import selector

html = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Design</title>
	<script type="text/javascript" src="js/conPanel.js"></script>
	<link rel="stylesheet" type="text/css" href="css/onLoad.css">
	<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
</head>
<body>
	<!-- 导航条 -->
	<div id="navbar">
		<img src="pic\logo.png" width="171px" height="50px" style="text-align: center;">
		<div class="navbar_L"  >
			<ul class="navbar_Ul">
				<li>CONTACT</li>
				<li>PAGES▼</li>
				<li>PROJECTS</li>
				<li>PRICE</li>
				<li>SERVICES</li>
				<li>ABOUT</li>
				<li style="color: #ae130c;">HOME</li>
				
			</ul>
		</div>
	</div>
	
	<!-- 幻灯图 -->
	<div class="ppt">
   
	</div>
 
	<!-- Our latest projects -->
	<!-- bootstrap -->
	<div class="container">
		<h2>Our latest projects</h2>
		<div class="pic_S">
			<div class="row">
				<div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">	
					<div class="picBox">
						<div style=" width:244.5px height:160px ">
							<img src="pic/news1.jpg"  width="100%" height=auto  >
						</div>
						<div>
							<p class="pic_p1" >Lorem ipsum</p>
							<p class="pic_p1 pic_p2" >
								Lorem ipsum dolor sit amet, conc tetu er adipi scing. Praesent ves tibuum molestie lacuiirhs. Aenean.
							</p>
							<a class="more" href="#">more</a>
						</div>
					</div>
				</div>
				<div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">	
					<div class="picBox">
						<div style=" width:244.5px height:160px ">
							<img src="pic/news2.jpg" width="100%" height=auto   >
						</div>
						<div>
							<p class="pic_p1">Lorem ipsum</p>
							<p class="pic_p1 pic_p2">
								Lorem ipsum dolor sit amet, conc tetu er adipi scing. Praesent ves tibuum molestie lacuiirhs. Aenean.
							</p>
							<a class="more" href="#">more</a>
						</div>
					</div>
				</div>
				<div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">	
					<div class="picBox">
						<div style=" width:244.5px height:160px ">
							<img src="pic/news3.jpg" width="100%" height=auto >
						</div>
						<div>
							<p class="pic_p1" >Lorem ipsum</p>
							<p class="pic_p1 pic_p2" >
								Lorem ipsum dolor sit amet, conc tetu er adipi scing. Praesent ves tibuum molestie lacuiirhs. Aenean.
							</p>
							<a class="more" href="#">more</a>
						</div>
					</div>
				</div>
				<div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">	
					<div class="picBox">
						<div style=" width:244.5px height:160px ">
							<img src="pic/news4.jpg" width="100%" height=auto >
						</div>
						<div>
							<p class="pic_p1" >Lorem ipsum</p>
							<p class="pic_p1 pic_p2">
								Lorem ipsum dolor sit amet, conc tetu er adipi scing. Praesent ves tibuum molestie lacuiirhs. Aenean.
							</p>
							<a class="more" href="#">more</a>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
 
	<!-- footer -->
	<!-- bootstrap -->
	<div class="container">
		<div class="row">
			<div class="col-md-4">
				<div style="padding: 0 15px">
					<h2 class="h2_Fond">About Us</h2>
					<p class="p_p">Perspiciatis unde omnis iste natus error sit voluptatem. Cum sociis natoque penatibus et magnis dis parturient montes ascetur ridiculus musull dui.</p>
					<p class="p_p">Lorem ipsumulum aenean noummy endrerit mauris. Cum sociis natoque penatibus et magnis dis parturient montes ascetur ridiculus mus. Null dui. Fusce feugiat malesuada odio.</p>
					<a href="#" class="more" >read more</a>
				</div>
			</div>
			<div class="col-md-4">
				<div style="padding: 0 15px">
					<h2 class="h2_Fond">Projects</h2>
					<div class="fUl">
						<ul >
							<li>Singapore Township</li>
							<li>Mega luxury Villas</li>
							<li>RNT Commercial Shopping Mall</li>
							<li>SVN Independent & Duplex Houses</li>
							<li>World wide IT park</li>
							<li>North Arena SNT Township</li>
						</ul>
					</div>
				</div>
			</div>
			<div class="col-md-4">
				<div style="padding: 0 15px">
					<h2 class="h2_Fond">Our Clients</h2>
					<div style="width:349px height:153px">
						<img src="pic\text.png" width="100%" height=auto>
					</div>
				</div>
 
			</div>
		</div>
	</div>
 
	<!-- 最底部 -->
	<!-- bootstrap -->
	<div class="big">
		<div class="container footerText">
			<div class="row">
				<div class="col-md-6 panel">
					<div>
						<p>
							<a class="footerP" href="index.html">Home</a> | 
							<a class="footerP" href="about.html">About</a> |
							<a class="footerP" href="services.html">Services</a> |
							<a class="footerP" href="price.html">Price</a> |
							<a class="footerP" href="projects.html">Projects</a> |
							<a class="footerP" href="contact.html">Contact</a>
						</p>
					</div>
				</div>
				<div class="col-md-6 panel">
					<div>
						<p>
							Copyright © 2016.Company name All rights reserved.More Templates 
							<a href="http://www.cssmoban.com/" target="_blank" style="color: #aaa;" >模板之家</a> 
							- Collect from 
							<a href="http://www.cssmoban.com/" title="网页模板" target="_blank" style="color: #aaa;">网页模板</a>
						</p>
					</div>
				</div>
			</div>
		</div>
	</div>
</body>
</html>"""


sel = selector.Selector(text=html)
# # 使用路径表达式查找，返回SelectorList对象
# tag_selector=sel.xpath("//*[@id='navbar']/div/ul/li")
# #把selectorlist变为 tag 用其.extract()方法,但是该方法生成的是一个列表,因为可能不止一个个tag(且该tag是字符串）
# tag_list=tag_selector.extract()
# tag=tag_list[0]


# 如果希望获取其中内容，则要在路径表达式最后加上/text()
# 同样的还要用.extract方法将SelectorList对象变成处理过的字符串格式
# tag_message=sel.xpath("//*[@id='navbar']/div/ul/li/text()").extract()
# print(tag_message[0])


# 还有要注意路径表达式的下标从 1 开始(确认过没有错)
# tag_message=sel.xpath("//div[@id='navbar']/div/ul/li[1]/text()").extract()


#xpath使得我们的解析可以变成可配置的解析
# name_xpath="//div[@id='navbar']/div/ul/li[1]/text()"
# tag_message=sel.xpath(name_xpath).extract()
# if tag_message:
#     print(tag_message[0])


# 指定属性选取
# href_message=sel.xpath("//a[@href='http://www.cssmoban.com/']/text()").extract()


# 输出属性而不是内容，将text()换成@属性名称
# footerP_message=sel.xpath("//a[contains(@class,'footerP')]/@class").extract()
# for info in footerP_message:
#     print(info)


# 或语句  |
footerP_and_more_message=sel.xpath("//a[contains(@class,'footerP')]/@class|//a[contains(@class,'more')]/@class").extract()
for info in footerP_and_more_message:
    print(info)



