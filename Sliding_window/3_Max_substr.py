# 1. substring -> contigous
# 2. substring not have repeating char

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        cnt = Counter()
        for right, x in enumerate(s):
            cnt[x] += 1
            while cnt[x] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right -left + 1)
        return ans

'''
Summarize:
    1. T: O(n), S: O(1)
'''