name='玛丽亚'
print(name)

#获取name的id类型
print('标识',id(name))  # 2633937837872  内存地址
print('类型',type(name))  # <class 'str'>
print('值',name)  # 玛丽亚


#赋值
name='处理并'

#多次赋值之后，变量指向新的空间。原来的空间的地址变成内存垃圾
