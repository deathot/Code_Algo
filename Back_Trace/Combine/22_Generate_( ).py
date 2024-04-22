'''
22. 括号生成

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

Tc:O(n*C(2n, n))
Sc:O(n)

Summarize:
    Method1:选或不选
        1.当左括号小于n时就可以选， 当右括号数小于左括号时就可以选
        2.边界是当i  == 2n 时结束
    Method2:枚举下一个选哪个
        pass
        
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        n2 = 2 * n
        path = [''] * n2
        def dfs(i, open):
            if i == n2:
                ans.append(''.join(path))
                return
            
            if open < n:
                path[i] = '('
                dfs(i+1, open + 1)
            
            if i - open < open:
                path[i] = ')'
                dfs(i + 1, open)
            
        dfs(0, 0)
        return ans
