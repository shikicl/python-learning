name='张三'
age=20

print(type(name),type(age))  #<class 'str'> <class 'int'>

#类型转换
print('我叫'+name+'今年，'+age+'岁')  #程序报错TypeError: can only concatenate str (not "int") to str
#纠错：将age转换成str
print('我叫'+name+'今年，'+str(age)+'岁')  #我叫张三今年，20岁

#1 -----------str()将其他类型转成str类型--
a=10
b=198.8
c=False
print(type(a),type(b),type(c))  #<class 'int'> <class 'float'> <class 'bool'>
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))  #10 198.8 False <class 'str'> <class 'str'> <class 'str'>



#2 -----------int()将其他类型转成int类型--
s1='128'  #字符串类型
f1=98.8
s2='72.77'
ff=True
s3='hello'

print(type(s1),type(f1),type(s2),type(ff),type(s3))  #<class 'str'> <class 'float'> <class 'str'> <class 'bool'> <class 'str'>
print(int(s1),type(int(s1)))  #将str转成int类型，条件：字符串为数字  #128 <class 'int'>
print(int(f1),type(int(f1)))  #float类型转为int类型，截取整数部分，舍掉小数部分  #98 <class 'int'>
# #小数串无法转成int类型
# print(int(s2),type(int(s2)))  #报错：ValueError: invalid literal for int() with base 10: '72.77'   #报错，因为字符串为小数串
print(int(ff),type(int(ff)))  #1 <class 'int'>

#下面报错，转换的时候字符串必须为数字串（而且必须为整数数字串）
#print(int(s3),type(int(s3)))  #报错：ValueError: invalid literal for int() with base 10: 'hello'  


#3 -----------float()将其他类型转成float类型--
s1='128.98'  #字符串类型
s2='76'
ff=True
s3='hello'
i=98
print(type(s1),type(s2),type(ff),type(s3),type(i))  #<class 'str'> <class 'str'> <class 'bool'> <class 'str'> <class 'int'>

print(float(s1),type(float(s1)))  #128.98 <class 'float'>
print(float(s2),type(float(s2)))  #76.0 <class 'float'>
print(float(ff),type(float(ff)))  #1.0 <class 'float'>
print(float(i),type(float(i)))  #98.0 <class 'float'>

#下面报错：字符串中的数据如果是非数字串，则不允许转换
print(float(s3),type(float(s3)))  #报错：ValueError: could not convert string to float: 'hello'



