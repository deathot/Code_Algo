'''
1. each num can be used once
2. the ans is unqiue 
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
            if x + nums[-3] + nums[-1] + nums[-2] < target:
                continue

            for j in range(i + 1, n - 2):
                y = nums[j]
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if x + y + nums[j + 1] + nums[j + 2] > target:
                    break
                if x + y + nums[-2] + nums[-1] < target:
                    continue
                   
                m = j + 1
                z = n - 1

                while m < z:
                    s = x + y + nums[m] + nums[z]
                    if s > target:
                        z -= 1
                    elif s < target:
                        m += 1
                    else:
                        ans.append([x, y, nums[m], nums[z]])
                        m += 1
                        while m < z and nums[m] == nums[m - 1]:
                            m += 1
                        z -= 1
                        while m < z and nums[z] == nums[z + 1]:
                            z -= 1
                
        return ans  

'''
Summarize:
    1. T: O(n^3) S: O(1)
    2. same as lc.15
'''  
        