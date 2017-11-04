# 通过select()直接传入CSS选择器即可完成选择
html = '''
<div class="paner">
    <div class = "panel_heading">
    <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.select('ul li'))
print(" ")
print(soup.select('#list-2,element'))
print(" ")
print(type(soup.select('ul')[0]))
print("========================")
for ul in soup.select('ul'):
    print(ul.select("li"))

#获取属性
for ul in soup.select('ul'):
    print(ul["id"])
    print(ul.attrs["id"])

 #获取内容
for li in soup.select("li"):
    print(li.get_text())

#总结
# 推荐使用lxml解析库,必要时使用html.parser
# 标签选择器筛选功能弱,但是速度快
# 建议使用find(),find_all()查询匹配单个结果或者多个结果
# 如果对CSS选择器熟悉建议使用select()
# 记住常用的获取属性和文本值的方法