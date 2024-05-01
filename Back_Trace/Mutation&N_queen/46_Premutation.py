'''
46. 全排列

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

TC:O(n * n!)
SC:O(n)

Summarize:
1.定义一个s数组， x = 下标i的s， 从而加到path中， 直到达到边界条件
2.不能用选或不选来做， 会丢失元素， 不能陷入回溯细节

'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0] * n
        ans = []
        
        def dfs(i,s):
            if i == n:
                ans.append(path.copy())
                return
            
            for j in s:
                path[i] = j
                dfs(i+1, s - {j})

        dfs(0, set(nums))
        return ans