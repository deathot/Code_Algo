'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            ans = numbers[left] + numbers[right]
            if ans == target:
                break
            elif ans > target:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]
'''