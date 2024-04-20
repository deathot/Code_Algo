'''
77. 组合

给定两个整数 n 和 k， 返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。

Tc:O(k*C(n, k))
Sc:O(k)

summarize:
    法1:选或不选
        1.递归边界是d == 0时， 即path路径已满
        2.选， 直接把i加到path中， 子问题就是递归i - 1之后的
        3.不选， 先判断path是否已满， 未满则不可不选
        4.回溯后需要先pop掉path中最后的数， 再进行下一步
        5.回溯的是上一次调用的函数， 但是递归的索引并没有减少， 所以判断的边界条件并不会发生改变
    法2:枚举要选的第j个
        pass
        
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        ans = []
        def dfs(i: int) -> None:
            d = k - len(path)
            if d == 0:
                ans.append(path.copy())
                return
            
            path.append(i)
            dfs(i - 1)
            path.pop()

            if i > d:
                dfs(i -1)
            
        dfs(n)
        return ans

