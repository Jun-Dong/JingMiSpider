import  re

#总结:尽量使用泛匹配,使用括号得到匹配的模板,尽量使用非贪婪模式
#有换行就用re.S


#泛匹配
# content = 'Hello 1234567 World_This is a Regex Demo'
#^:以xx开头
#$:以xx结尾
#.:	匹配除“\n”之外的任何单个字符。要匹配包括“\n”在内的任何字符，请使用像“(.|\n)”的模式。
#*:匹配N次
#.*:匹配n次任意字符
# result = re.match('^Hello.*Demo$',content)
# print (result)
# print (result.group())#匹配结果
# print (result.span())#匹配长度
#()匹配括号内的表达式,也表示一个组


#匹配目标
#\s匹配空白符
#\d配一个数字字符。等价于[0-9]。
#+匹配前面的子表达式一次或多次
#\d+匹配多次\d
#(pattern)匹配pattern并获取这一匹配。
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\s.*Demo$',content)
# print (result)
# print (result.group())#匹配结果
# print (result.group(1))#匹配结果
# print (result.span())#匹配长度

#贪婪匹配 .*匹配尽可能多的字符 group(1):7
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$',content)
# print (result)
# print (result.group(1))


#非贪婪匹配 .*匹配尽可能少的字符 group(1):1234567
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$',content)
# print (result)
# print (result.group(1))

#匹配模式
#re.S不加报错,因为.匹配除换行符的所有字符
# content = "Hello 1234567 World_This  \n is a Regex Demo"
# result = re.match('^He.*?(\d+).*?Demo$',content)
# print (result)
# print (result.group(1))

# content = "Hello 1234567 World_This  \n is a Regex Demo"
# result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
# print (result)
# print (result.group(1))

#转义
# content = 'price is $5.00'
# result = re.match('price is $5.00',content)
# print(result) 结果为None
content = 'price is $5.00'
result = re.match('price is \$5\.00',content)
print(result)
print(result.group())
