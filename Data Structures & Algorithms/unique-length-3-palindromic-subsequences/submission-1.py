class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # edge case
        if len(s) < 3:
            return 0
        palindrome = 0

        first = [float('inf')] * 26
        last = [float('-inf')] * 26

        for index, c in enumerate(s):
            first[ord(c) - 97] = min(first[ord(c) - 97], index)
            last[ord(c) - 97] = max(first[ord(c) - 97], index)
        
        for l, r in zip(first, last):
            if r - l >= 2:
                unique = len(set(s[l + 1: r])) # 26 times atmost
                palindrome += unique
        
        return palindrome
        
