import re
content = 'Extra stings Hello 1234567 World_This is a Regex Demo'
# result = re.match('Hello.*?(\d+).*?Demo',content)
# print(result)
result = re.search('Hello.*?(\d+).*?Demo',content)
results = re.findall('Hello.*?(\d+).*?Demo',content)#以列表形式返回全部符合结果

print(result)
print(result.group(1))

print(results)
print(type(results))
for result2 in results:
    print(result2)
#search找到符合的字符串
#总结:能用search不用match