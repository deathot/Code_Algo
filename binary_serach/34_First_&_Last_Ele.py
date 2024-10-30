leetcode_34_在排序数组中查找元素的第一个和最后一个位置

时间复杂度:o(logn)
空间复杂度:o(1)

总结:
1.三种写法（左开右开， 左闭右闭， 左闭右开）
2.四种类型（对于 target 来说存在>, >=, <, <=）
3.类里调用是局部变量， 需类外调用方可使用

def st_en(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = st_en(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = st_en(nums, target + 1) - 1
        return [start, end]

# review
def func(nums: List[int], target: int) -> int:
    n = len(nums)
    l = 0
    r = n-1

    while l <= r:
        m = (l+r) // 2
        if nums[m] < target:
            l = m+1
        else:
            r = m-1
    return l

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fir = func(nums, target)
        if fir == len(nums) or nums[fir] != target:
            return [-1, -1]
        las = func(nums, target+1) - 1
        return [fir, las] 