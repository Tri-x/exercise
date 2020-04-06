from string import *#引入字符模块
from random import *
#统计字符数
str_dict={}
strings=''
for x in range(randint(0,200)):#随机字符随机长度
	strings+=printable[randint(0,len(printable)-6)]
#string.printable='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
print(strings)
for x in range(len(set(strings))):#计数每个字符出现的次数储存在字典中一一对应
	str_dict[list(set(strings))[x]]=strings.count(list(set(strings))[x])
for strss,nums in str_dict.items():#格式化输出
	print('{0}:{1}'.format(strss,nums),end='|')
