class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        # cnts = [[0] * 11 for _ in range(n)]
        # for x, y in pick:
        #     cnts[x][y] += 1
        
        # ans = 0
        # for i, cnt in enumerate(cnts):
        #     if any(c > i for c in cnt):
        #         ans += 1
        # return ans

        ans = 0
        cnts = [[0] * 11 for _ in range(n)]
        won = [False] * n
        for x, y in pick:
            cnts[x][y] += 1
            if not won[x] and cnts[x][y] > x:
                won[x] = True
                ans += 1
        return ans
