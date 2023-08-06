#输出数字
print(520)
print(1.3)

#可以输出字符串
print('helloworld')
print("helloworldhelloworld")

#将数据输出到文件中
#注意点：
#1.指定的盘符存在
#2.使用file=fp
fp=open('d:/text.txt','a+')#a+：如果文件不存在创建文件；如果文件存在追加
print('helloworld',file=fp)
fp.close()

#不换行输出（输出内容在一行中）
print('hello','1','1')
