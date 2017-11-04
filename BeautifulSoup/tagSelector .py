from bs4 import BeautifulSoup

# html = """
# <html><head><title>The Dormouse's strory</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's strory</b></p>
# <p class="story">xxxxxxxxxxxxxxxxxxxddddddddddddddddddddaaaaaaaaaaa
# <a href="http://www.baidu.com" class="sister" id="link1"><!--Elsie--></a>
# and they lived at the bottom of awell</p>
# <p class="story">...</p>
# </body>
# """
#
# soup = BeautifulSoup(html,"lxml")
# print(soup.prettify())#格式化html 调整代码 如加了</html>
# print(soup.title.string)


html = """
<html><head><title>The Dormouse's strory</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's strory</b></p>
<p class="story">xxxxxxxxxxxxxxxxxxxddddddddddddddddddddaaaaaaaaaaa
<a href="http://www.baidu.com" class="sister" id="link1"><!--Elsie--></a>
and they lived at the bottom of awell</p>
<p class="story">...</p>
</body>
"""

soup = BeautifulSoup(html,"lxml")
# print(soup.title)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)#如果多个,只返回第一个匹配结果
# #获取属性
# print(soup.p.attrs['name'])#结果一样
# print(soup.p['name'])
# #获取内容
# print(soup.p.string)#第一个P标签的文字
# #嵌套选择
# print(soup.head.title.string)#层层迭代,进行选择
#
# #子节点和子孙节点
# print(soup.p.contents)#标签所有的子节点,返回类型为list
# print(soup.p.children)#标签所有的子节点,返回类型为迭代器
# for i in enumerate(soup.p.children):
#     print(i)

#父节点和祖先节点
#print(type(soup.a.parent))
#print(soup.a.parent)#获取第一个a标签
#print(soup.a.parents)
#print(list(enumerate(soup.a.parents)))#祖先节点迭代器

#兄弟节点
# print(list(enumerate(soup.a.next_siblings)))
# print(list(enumerate(soup.a.previous_siblings)))