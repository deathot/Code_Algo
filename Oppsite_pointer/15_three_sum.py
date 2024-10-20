'''
1. ans can't be same
2. index can't be reused
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            x = nums[i]
            if i > 0 and nums[i - 1] == x:
                continue
            elif x + nums[-1] + nums[-2] < 0:
                continue
            elif x + nums[i] + nums[i + 1] > 0:
                break
            
            j = i + 1
            k = n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
        return ans

'''
Summarize:
    1. T: O(n^2)  S: O(1)
    2. oppsite two pointer task
    3. first, sort the nums then loop n-2 times for i, 
       finally if find ans , ennumerate j + 1 and k - 1, be sure don't miss any ans.
'''