class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        left = 0
        right = n - 1
        ans = min(height[left], height[right]) * (right - left)

        while left < right:
            area = (right - left) * min(height[left], height[right])
            ans = max(area, ans)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
        #     if height[left] < height[right]:
        #         mul = height[left + 1] * (right- left + 1)
        #         if mul > ans:
        #             ans = mul
        #             left += 1
        #     else:
        #         mul1 = height[right - 1] * (right - 1 - left)
        #         if mul1 > ans:
        #             ans = mul1
        #             right -= 1
        # return ans 
                
'''
Summarize:
    T: O(n)
    S: O(1)
'''       