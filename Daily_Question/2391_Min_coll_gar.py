class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = sum(map(len, garbage)) + sum(travel) * 3
        for c in "MPG":
            for g, t in zip(reversed(garbage), reversed(travel)):
                if c in g:
                    break
                ans -= t  # 没有垃圾 c，多跑了
        return ans
