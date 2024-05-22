class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set(x for m in matches for x in m)
        loss_count = Counter(loser for _, loser in matches)
        return [sorted(x for x in players if x not in loss_count),
                sorted(x for x, c in loss_count.items() if c == 1)]
