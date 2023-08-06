# 转义字符

print('hello\nworld') # \n换行

print('hello\tworld') #\t表示制表符：特殊的空白字符，在文本中添加水平距离
print('helloooo\tworld') 

print('hello\rworld') #world 将hello进行了覆盖
print('hello\bworld') #\b退一个格子，o没了

#网址：
print('http:\\\\www.baidu.com')

#为了在字符串中输出单引号,此处的\表述字符串应该输出的内容
print('老师说:\'大家好\'')

#原字符，不希望字符串中的转义字符起作用。
#原字符：在字符串之前加上r或者R
print(r'hello\nworld')

#最后一个字符不能是单个反斜线
# print(r'hello\nworld\')
#可以是双反斜线
print(r'hello\nworld\\')
