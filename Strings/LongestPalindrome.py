# Leetcode 5

class Solution:
    # Brute Force
    def longestPalindromeBruteForce(self, s: str) -> str:
        if len(s) == 1: return s

        long_pal = 1
        pal = s[0]
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if j-i+1 > long_pal and s[i:j+1] == s[i:j+1][::-1]:
                    long_pal = j-i+1
                    pal = s[i:j+1]

        return pal

    #Expand Around Center
    def longestPalindromeExpandAroundCenter(self, s: str) -> str:
        if len(s) == 1: return s

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        maxStr = s[0]
        for i in range(len(s) - 1):
            odd = expand(i, i)
            even = expand(i, i+1)

            if len(odd) > len(maxStr):
                maxStr = odd
            if len(even) > len(maxStr):
                maxStr = even