class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st = []
        for i, x in enumerate(nums):
            while st and x < st[-1] and len(st) + len(nums) - i > k:
                st.pop()
            if len(st) < k:
                st.append(x)
        return st
