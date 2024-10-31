# citations >= nums of paper -> nums[mid] >= right - left + 1

class Solution:
    def hIndex(self, citations: List[int]) -> int:
            
        n = len(citations)
        right = n
        left = 1
        
        while left <= right:
            mid = (right + left) // 2
            
            if citations[-mid] >= mid:
                left = mid + 1
            else:
                right = mid - 1
        return right

'''
1. T: O(logn), S: O(1)
'''