import requests
import re
content = requests.get('https://book.douban.com/').text
#print(content)
#从网页源代码提取书名等
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span',re.S)
results = re.findall(pattern,content)
#print(results)
for result in results:
    url,name,author,date= result
    # author = re.sub('\s','',author)练习re.sub去掉换行符
    # date =  re.sub('\s','',date)
    print(url,name,author.strip(),date.strip())#strip()去掉换行符