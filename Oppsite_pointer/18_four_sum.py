'''
1. each num can be used once
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n - 3):
            x = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if x + nums[i + 3] + nums[i + 1] + nums[i + 2] > target:
                break
            if x + nums[j - 3] + nums[j - 1] + nums[j - 2] < target:
                continue

            for j in range(n - 3):
                y = nums[::j]
                if j > 0 and nums[j] == nums[j + 1]:
                    continue
                if x + y + nums[i + 1] + nums[i + 2] > target:
                    continue
                if x + y + nums[j - 1] + nums[j - 2] < target:
                    break

                    

                m = i + 1
                n = j - 1

                while m < n:
                    s = x + y + nums[m] + nums[n]
                    if s > target:
                        m -= 1
                    elif s < target:
                        n += 1
                    else:
                        ans.append([x], [y], nums[m], nums[n])
                        m += 1
                        while m < n and nums[m] == nums[m - 1]:
                            m += 1
                        n -= 1
                        while m < n and nums[n] == nums[n + 1]:
                            n -= 1
                
        return ans    