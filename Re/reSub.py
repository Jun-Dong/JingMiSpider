#re.sub
#替换字符串每一个匹配的子串后返回替换后的字符串
import re

# content = 'Extra stings Hello 1234567 World_This is a Regex Demo'
# content = re.sub('\d+','',content)
# print(content)

#\1把第一个括号里面的内容替换
#r保留原生字符
content = 'Extra stings Hello 1234567 World_This is a Regex Demo'
content = re.sub('(\d+)',r'\1 8910',content)
print(content)
