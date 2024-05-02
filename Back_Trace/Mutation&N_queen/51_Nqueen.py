'''
51. N 皇后

按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

Tc:o(n^2 * n!)
Sc:o(n)

Summarize:
1.思考nqueen的特性以及规律， 那么就是每行每列只有一个queen， 那么就先遍历循环所有可能的情况， 而后再去筛选有效的queen。
2.筛选所需思考的是， 如何表达在某一个queen在r行c列确定后， 他的左上以及右上是否有queen， 那么可以表示为r行之前的每一行的queen所在位置的R+C 是否等于当前循环遍历的r + c, 从而来检查是否是有效的queen
3.set(range(n))的意思是创建一个list = {0 到 n -1}

'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = [0] * n

        def valid(r, c):
            for R in range(r):
                C = col[R]
                if r+c == R+C or r-c == R-C:
                    return False
            return True

        def dfs(r, s):
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n-c-1) for c in col])
                return
            
            for c in s:
                if valid(r, c):
                    col[r] = c
                    dfs(r+1, s-{c})
            
        dfs(0, set(range(n)))
        return ans

