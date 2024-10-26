class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        array1 = [0] * n
        array1[0] = height[0]
        ans = 0

        for i in range(1, n):
            array1[i] = max(array1[i - 1], height[i])

        array2 = [0] * n
        array2[n - 1] = height[n - 1]

        for j in range(n - 2, -1, -1):
            array2[j] = max(array2[j + 1], height[j])
        
        for h, ar1, ar2 in zip(height, array1, array2):
            ans += min(ar1, ar2) - h
        
        return ans

'''
Summarize:
    1. T: O(n), S: O(n)
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        ary1 = 0
        ary2 = 0
        i = 0
        j = n - 1
        while i <= j:
            ary1 = max(ary1, height[i])
            ary2 = max(ary2, height[j])
            if ary1 < ary2:
                ans += ary1 - height[i]
                i += 1
            else:
                ans += ary2 - height[j]
                j -= 1
        return ans

'''
Summarize:
    1. T: O(n), S: O(1)
'''

        # n = len(height)
        # ans = 0
        # count = 0
        # block = 0
        # for i in range(n - 1):
        #     if i > 0 and height[i - 1] < height[i]:
        #         i += 1
        #     while height[i + 1] < height[i] < height[i - 1]:
        #         left = i
        #         i += 1
        #         count += 1
        #         right = i + 1
        #         for j in range(left, right - 1):
        #             block += height[j]
        #         ans += min(height[left], height[right]) * count - block
            
        #     if height[i] < height[i - 1] and height[i] < height[i + 1] and height[i - 1] == height[i + 1]:
        #         ans += height[i + 1] - height[i]
        #         i += 1
        # return ans
