class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed = ""
        for c in s:
            if c.isalnum():
                trimmed+= c
        trimmed = trimmed.lower()
        l, r = 0, len(trimmed) - 1
        while l < r:
            if trimmed[l] != trimmed[r]:
                return False
            l += 1
            r -= 1
        
        return True