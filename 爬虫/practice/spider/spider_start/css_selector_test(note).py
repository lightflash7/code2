from scrapy import Selector

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


# 和xpath类似
sel = Selector(text=html)
# footerP_selector_list=sel.css(".footerP")
# footerP_tag=footerP_selector_list.extract()


# 打印文本内容在最后面用  ::text
# footerP_text=sel.css(".footerP::text").extract()


# 选择第二个元素，nth-child 父亲的儿子，就是自己这一辈的第二个元素,返回一个列表
# footerP_text=sel.css(".footerP:nth-child(2)::text").extract()


# 选择跟在p后面的a元素
# p_a_text=sel.css("p>a::text").extract()


# 选择a前紧跟着有p的兄弟a
# p_a_text=sel.css("p+a::text").extract()


# 选择p后面的所有兄弟a元素
# p_a_text=sel.css("p~a::text").extract()


#根据别的属性选则
# p_a_text=sel.css("a[href='http://www.cssmoban.com/']::text").extract()

a_footerP_text=sel.css("a.footerP::text").extract()
for info in a_footerP_text:
    print(info)
pass

