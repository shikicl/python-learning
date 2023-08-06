#-------------------------------输入函数input()的使用---
p=input("想要什么礼物呢")  #()中的内容为对用户输入的提示语
print(p)
print(type(p)) 

'''
输出：
想要什么礼物呢金箍棒
金箍棒
<class 'str'>
'''

#----------------------输入函数input()的高级使用----
a=input('请输入一个加数：')
b=input('请输入另一个加数：')
print(a+b,type(a+b))  #12 <class 'str'> #此处的➕ 是一个连接作用
#打印上面变量的类型
print(type(a),type(b))  #<class 'str'> <class 'str'>

#类型转换方式1
a=int(a)
b=int(b)
print(a+b)

#类型转换方式2
c=int(input('请输入一个数'))
d=int(input('请输入一个数'))
print(c+d)


#----------------------python中常用的运算符----
#----------------------算术运算符----
#加减乘除
print(1+1)
print(1-1)
print(1*19)
print(9/3)

print(11//2)  #整除运算
print(11%2)  #取余运算
print(2**2)  #2的平方

print(9//4)  #2
print(-9//-4)  #2

print(9//-4)  #-3
print(-9//4)  #-3  一正一负的整数公式，向下取整

print(9%-4) #-3 公式：余数=被除数-除数*商  9-(-4)*(-3)  9-12=-3
print(-9%4)  #3  -9-4*(-3)  -9+12=3

#----------------------赋值运算符----
#链式赋值
a=b=c=20
print(a,id(a)) #20 2423653362576
print(b,id(b)) #20 2423653362576
print(c,id(c)) #20 2423653362576

#参数赋值
a1=20
a1+=30
print(a1)  #相当于a1=a1+30  #50
a1-=45
print(a1)  #相当于a1=a1-45  #5
a1*=2
print(a1)  #相当于a1=a1*2  #10
a1/=3
print(a1)  #相当于a1=a1/3  #3.3333333333333335
print(type(a1))  #<class 'float'>
a1//=2
print(a1)  #由于上面已经是float类型，所以整除运算之后也是float类型

#解包赋值
a,b,c=20,30,40
print(a,b,c)  #20 30 40  #对应

#交换两个变量的值
a,b=10,20
print('交换之前',a,b)

a,b=b,a
print('交换之后',a,b)


#----------------------比较运算符----


##############学到P24  https://www.bilibili.com/video/BV1wD4y1o7AS/?p=24&spm_id_from=pageDriver&vd_source=cdf4f86d98272a70808fd09817f0fcd2
