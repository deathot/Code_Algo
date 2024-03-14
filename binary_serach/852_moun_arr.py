852_山峰数组

时间复杂度o(logn)
空间复杂度o(1)

总结:
1.二分查找最大值
2.大于i - 1 = 大于i - 1 后所有数 反之 i + 1

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = -1
        right = len(arr)
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid
        return right