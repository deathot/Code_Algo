'''
1. return num[string] == n
2. each string cannot have consecutive zero 
3. each string just have 0 and 1
'''
class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        path = [''] * n

        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return

            path[i] = '1'
            dfs(i + 1)

            if i == 0 or path[i - 1] == '1':
                path[i] = '0'
                dfs(i + 1)
        
        dfs(0)
        return ans
