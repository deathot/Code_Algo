'''
494. 目标和

给你一个非负整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

Tc:o(n * (target + s))
Sc:o(n * (target + s))

'''
'''
def one_zero_knapsack(capacity: int, w: List[int], v: List[int]) -> int:
    n = len(w)

    @cache
    def dfs(i, c):
        if i < 0:
            return 0

        if w[i] > c:
            return dfs(i - 1, c)
        
        return max(dfs(i - 1, c), dfs(i - 1, c - w[i] + v[i])

    return dfs(n - 1, capacity)
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # t = p - (s - p)
        # 2p = t + s
        # p = (t + s) // 2 -> target

        target += sum(nums)
        if target < 0 or target % 2 != 0:
            return 0
        target //= 2
        n = len(nums)
        
        @cache
        def dfs(i , c):
            if i < 0:
                return 1 if c == 0 else 0

            if nums[i] > target:
                return dfs(i - 1, target)
            
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])

        return dfs(n - 1, target)

# o法二 记忆化 -> 递推 o(n * (target + s)) & o(n * (target + s))
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        + = p
        - = s - p
        t = + - - -> p - (s - p) = 2p - s
        p = (t + s) // 2
        
        '''
        target += sum(nums)
        if target < 0 or target % 2 != 0:
            return 0
        target //= 2
        n = len(nums)

        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1
        
        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = f[i][c] + f[i][c - x]
        
        return f[n][target]
#o(target)空间优化 只需要两行就可以计算所以可能方法， 所以初始化两行， 而后每一个i都 % 2 (i只有0, 1两个val， 所以就相当于是f2 = f1, f2 = f0, 那么f1变为当前节点， f2 == f0变为下一个节点)总之就是f1 -> f0, f0 -> f1.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        + = p
        - = s - p
        t = + - - -> p - (s - p) = 2p - s
        p = (t + s) // 2
        
        '''
        target += sum(nums)
        if target < 0 or target % 2 != 0:
            return 0
        target //= 2
        n = len(nums)

        f = [[0] * (target + 1) for _ in range (2)]
        f[0][0] = 1
        
        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    f[(i + 1) % 2][c] =  f[(i) % 2][c]
                
                else:
                    f[(i + 1) % 2][c] =  f[(i) % 2][c] + f[(i) % 2][c - x]

        return f[(n) % 2][target]

#o(target + s) 空间优化2 只需要一个数组
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        + = p
        - = s - p
        t = + - - -> p - (s - p) = 2p - s
        p = (t + s) // 2
        
        '''
        target += sum(nums)
        if target < 0 or target % 2 != 0:
            return 0
        target //= 2

        f = [1] + [0] * target
        
        for x in nums:
            for c in range(target, x - 1, -1):
                    f[c] += f[c - x]

        return f[target]

    

