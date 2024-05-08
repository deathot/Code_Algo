'''
2079. 给植物浇水

pass

Tc:
Sc:

Summarize:

'''
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = len(plants)
        cap = capacity
        for i, x in enumerate(plants):
            if cap < x:
                ans += i * 2
                cap = capacity

            cap -= x

        return ans