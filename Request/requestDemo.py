import json

import requests

# response = requests.get("http://www.baidu.com")
# print(type(response))
# print(response.status_code)#状态码
# print(type(response.text))#响应内容类型
# print(response.text)#响应内容
# print(response.cookies)

# 各种请求方式
# requests.post("httP://httpbin.org/post")
# requests.put("httP://httpbin.org/put")
# requests.delete("httP://httpbin.org/delete")
# requests.head("httP://httpbin.org/get")
# requests.options("httP://httpbin.org/get")

# 基本GET请求
# 基本写法
# response = requests.get('http://httpbin.org/get')
# print(response.text)
# 带参数GET请求
# (1)
# response = requests.get('http://httpbin.org/get?name=Jadon&age=20')
# print(response.text)
# (2)比较简单的方式
# data = {
#     'name':'Jadon',
#     'age': 20
# }
# response = requests.get("http://httpbin.org/get",params=data)
# print(response.text)
# 解析json
# response = requests.get("http://httpbin.org/get")
# print(type(response.text))#原本为str
# print(response.json())
# print(json.loads((response.text)))#转码为json
# print(type(response.json()))
# 获取二进制数据
# response = requests.get('http://github.com/favicon.ico')
# print(type(response.text), type(response.content))
# print(response.text)
# print(response.content)  # 获取二进制内容
# 保存图片
# with open('favicon.ico','wb') as f:
#     f.write(response.content)
#     f.close()
# 添加headers
# response = requests.get('http://www.zhihu.com/explore')
# print(response.text)#会报500错误
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
# }
# response = requests.get('http://www.zhihu.com/explore',headers = headers)
# print(response.text)
# 基本post请求
# data = {'name': 'Jadon', 'age': 20}
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
# }
# response = requests.post('http://httpbin.org/post', data=data, headers=headers)
# print(response.json())
# 响应
# reponse属性
# response = requests.get('http://www.jianshu.com')
# print(type(response.status_code),response.status_code)
# print(type(response.headers),response.headers)
# print(type(response.cookies),response.cookies)
# print(type(response.url),response.url)
# print(type(response.history),response.history )
# 状态码判断
# response = requests.get('http://www.jianshu.com')
# exit() if not response.status_code == 200 else print('Request Successfully')
# exit() if not response.status_code == requests.codes.ok else print('Request Successfully')

# 高级操作
# 文件上传
# files = {'file': open('favicon.ico','rb')}
# response = requests.post('http://httpbin.org/post',files=files)
# print(response.text)
# #获取cookie
# response = requests.get('http://www.baidu.com')
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key + '=' +value)

# 会话维持
# 模拟登录
# requests.get('httP://httpbin.org/cookies/set/number/27315')#设置cookies
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)#请求了2次相当于不同浏览器打开,所以cookies为空
#
# s = requests.Session()#加个Sussion解决
# s.get('httP://httpbin.org/cookies/set/number/27315')#设置cookies
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

# 证书验证
# from requests import urllib3
# urllib3.disable_warnings()#消除警告信息
# response = requests.get('http://www.12306.cn',verify=False)#verify=False 不检查证书
# print(response.status_code)
# response = requests.get('http://www.12306.cn',cert=('/path/server.crt','path/key'))#手动指定证书,本地没有证书
# print(response.status_code)

# 代理设置 ip不稳定,访问成功有偶然性
# proxies = {
#     'https':'https://115.233.210.218:808',
#     'http':'http://122.224.227.202:3128'
# }
# response = requests.get('http://www.taobao.com', proxies=proxies)
# print(response.status_code)

#超时设置 超出则报错
# from requests.exceptions import ReadTimeout
#
# try:
#     response = requests.get('http://www.taobao.com',timeout = 1)
#     print(response.status_code)
# except ReadTimeout:
#     print('Timeout')
#认证设置
from  requests.auth import HTTPBasicAuth
r = requests.get('http://120.27.34.24:9001',auth=HTTPBasicAuth('user',123))
print(r.status_code)
# r = requests.get('http://120.27.34.24:9001',auth=('user','123'))#字典形式
# print(r.status_code)
