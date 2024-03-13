33_搜索旋转排序数组

时间复杂度o(logn)
空间复杂度o(1)

总结:
1.分类讨论， 共五种， 结果只有两种-left = mid或者 right = mid
2.布尔表达式， 来判定结果
3.左开右开区间， right要返回ans， 所以 退出循环的条件是 left + 1 < right


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i: int) -> bool:
            end = nums[-1]
            if nums[i] > end:
                return  target > end and nums[i] >= target
            else:
                return target > end or nums[i] >= target
            
        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid
        if right == len(nums) or nums[right] != target:
            return -1
        return right 