'''
216. 组合总和 III

找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
只使用数字1到9
每个数字 最多使用一次 
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

Tc:O(k*C(9, k))
Sc:O(k)

Summarize:
    Method1:选或不选
        1.边界条件为 d == 0时， 即path满时， 减枝思路为t < 0 或 n项和还是 < t
        2.递归所需参数需要一个t， 来判断是否加入ans

    Method2:枚举下一个要选的
        pass
        
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        
        def dfs(i, t):
            d= k - len(path)
            if t < 0 or t > d * (2*i - d + 1) // 2:
                return
            if d == 0:
                ans.append(path.copy())
                return
            
            path.append(i)
            dfs(i - 1, t - i)
            path.pop()

            if i > d:
                dfs(i - 1, t)
            
        dfs(9, n)
        return ans
