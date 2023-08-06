#1 整数类型
n1=90
n2=-76
n3=0

print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

#整数可以表示为二进制，十进制，八进制，十六进制
print('十进制',118)  #输出：十进制 118
print('二进制',0b10101111) #二进制0b开头   #输出：二进制 175
print('八进制',0o176)  #八进制0o开头   #输出：八进制 126
print('十六进制',0x1EAF)  #十六进制0x开头   #输出：十六进制 7855

#--------------------------------------------------------------
#2 浮点数类型
a1=3.14159  #3.14159 <class 'float'>
print(a1,type(a1))  

a2=1.1
a3=2.2
print(a2+a3)  #3.3000000000000003
#浮点数的相加相减会出现上面的输出并不是理想精确的输出


#下面能够得到想要的输出
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))  #3.3

#--------------------------------------------------------------
#3 Boolean类型
#值为true或者false；true表示整数1.false表述0
f1=True
f2=False
print(f1,type(f1))  #True <class 'bool'>
print(f2,type(f2))  #False <class 'bool'>

#转成整数计算
print(f1+1)  #2 
print(f2+1)  #1

#--------------------------------------------------------------
#4 字符串类型
#单引号和双引号定义的字符串必须在一行显示
#三引号定义的字符串可以分布在多行显示

str1='人生苦短，我会飞'
str2="人生苦短，我会飞"

str3="""人生苦短，
我会飞"""

str4='''人生苦短，
我会飞'''

print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))
