cnt = 5
for _ in range(cnt // 2):
    print("ok")

a = False
b, c  = 6, 2
if a and b > c:
    print("ok2")
else:
    print("ok3")

class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int: