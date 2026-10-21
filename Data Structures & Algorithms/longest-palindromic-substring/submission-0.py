class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l <= r and l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            print(s[l + 1: r])
            return s[l + 1: r]
        res = ""
        resLen = 0
        for i in range(len(s)):
            # odd length
            odd = expand(i, i)
            # even length 
            even = expand(i, i + 1)
            if len(odd) > resLen:
                res = odd
                resLen = len(odd)
            if len(even) > resLen:
                res = even
                resLen = len(even)
        return res 