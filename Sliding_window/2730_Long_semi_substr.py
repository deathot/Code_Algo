class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 1
        left = 0
        rep = 0

        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                rep += 1

            if rep > 1:
                left += 1
                while s[left] != s[left - 1]:
                    left += 1
                rep = 1
            ans = max(ans, right - left + 1)

        return ans    
    
'''
Summarize:
    1. T: O(n), S: O(1)
'''