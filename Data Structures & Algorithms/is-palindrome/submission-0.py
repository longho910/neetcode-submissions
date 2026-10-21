class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''.join(c for c in s.lower() if c.isalnum())
        return newS == newS[::-1]