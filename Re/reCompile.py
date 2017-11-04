import re
#re.compile
#将正则字符串编译成正则表达式对象
content = 'Hello 1234567 World_this\n is aRegex Demo'
pattern = re.compile('Hello.*Demo',re.S)
result = re.match(pattern,content)

#result = re.match('Hello.*Demo',content,re.S)和上面的结果一样
print(result)