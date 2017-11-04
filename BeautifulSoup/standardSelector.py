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

soup = BeautifulSoup(html, "lxml")
# print(soup.find_all('ul'))
# print("============================")
# print(soup.find_all('ul')[0])
# 嵌套查找
# for ul in soup.find_all('ul'):
#     print(ul.find_all('li'))

# print(soup.find_all(attrs={'id':'list-1'}))
# print("============================")
# print(soup.find_all(attrs={'name':'elements'}))
#print(soup.find_all(class_='element'))  # class要加_因为它是关键字
print(soup.find('ul'))
