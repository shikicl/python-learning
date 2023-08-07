#python普通函数的定义和python中类的定义不同，调用方式不同

#普通函数的定义：findRepeatNumber被定义为普通函数（独立函数），没有self参数。

def findRepeatNumber(nums: [int]) -> int:
    # 函数体
    # ...
    return -1
#调用方式：可以直接通过函数名来调用，不需要创建类的实例对象。
nums = [2, 3, 1, 0, 2, 5, 3]
result = findRepeatNumber(nums)
print("重复数字：", result)



#类的方法定义和调用：findRepeatNumber被定义为被定义为类MyClass的方法。带有self参数，用于引用类的实例对象
class MyClass:
    def findRepeatNumber(self, nums: [int]) -> int:
        # 方法体
        # ...
        return -1
#调用方式：需要先创建类MyClass的实例对象，然后通过实例对象来调用方法。
my_instance = MyClass()
nums = [2, 3, 1, 0, 2, 5, 3]
result = my_instance.findRepeatNumber(nums)
print("重复数字：", result)
