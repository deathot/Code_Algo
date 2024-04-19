'''
131. 分割回文串

给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 
回文串。返回 s 所有可能的分割方案。

时间复杂度
空间复杂度

summarize:
1.

'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)
        
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            
            for j in range(i, n):
                t = s[i : j + 1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j + 1)
                    path.pop()


        dfs(0)
        return ans