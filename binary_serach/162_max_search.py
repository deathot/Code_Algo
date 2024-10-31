leetcode_162_峰值元素是指其值严格大于左右相邻值的元素。


时间复杂度:o(logn)
空间复杂度:o(1)

总结:
1.左开右开区间

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) //2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        return right


# num[mid] < mid + 1: l = mid + 1
# numd[mid] < mid - 1: r = mid - 1

# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         l = 0
#         n = len(nums)
#         r = n - 1

#         while l < r:
#             mid = (l + r) // 2
            
#             if nums[mid] < nums[mid + 1]:
#                 l = mid + 1
#             elif nums[mid] > nums[mid - 1]:
#                 r = mid - 1
#             elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
#                 mid = (l + r) // 2
#                 break

#         return 0 if n == 1 else mid

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        return right

            
        