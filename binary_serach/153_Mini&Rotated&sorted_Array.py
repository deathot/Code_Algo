153_寻找旋转排序数组中的最小值

时间复杂度o(logn)
空间复杂度o()1

总结:
1.左开右闭区间
2.旋转数组两种情况 0- 7，4-7——0-2
3.所有数与最右元素比较， 最右要么为最小值， 要么在最小值右侧

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = -1
        right = n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid
            else:
                right = mid
        return nums[right] 
