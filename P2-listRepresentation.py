#对下文中函数的定义：def twoSum(self, nums: List[int], target: int) -> List[int]:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []

#问题1：def twoSum(self, nums: List[int], target: int) -> List[int]:和def twoSum(self, nums: [int], target: int) -> [int]:是一样的吗？
#答：是一样的。

#问题2：def twoSum(self, nums: List[int], target: int) -> List[int]:和def twoSum(self, nums: [int], target: int) -> int:是一样的吗？
#答：是不一样的。

#区别在于：整数和整数列表。[int]表示整数列表；int 表示整数
#def twoSum(self, nums: List[int], target: int) -> List[int] 
#表示 twoSum 方法接受一个整数列表 nums 和一个目标整数 target 作为输入参数，并返回一个整数列表作为结果。方法的返回类型为 List[int]，即一个整数列表。
#def twoSum(self, nums: [int], target: int) -> int 
#表示 twoSum 方法接受一个名为 nums 的参数，该参数是一个由整数构成的列表，以及一个目标整数 target 作为输入。方法的返回类型为 int，即一个整数。

#注意：     
#在 Python 中，List[int] 表示一个整数列表类型，而 [int] 也表示一个整数列表类型。这两者在类型注解中是等价的，都用于指定方法的返回类型为一个整数列表。
