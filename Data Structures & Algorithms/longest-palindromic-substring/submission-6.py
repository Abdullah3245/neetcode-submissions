class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_string = ""
        length = 0

        def longest(l, r):
            nonlocal longest_string
            nonlocal length
            count = 0

            if r == len(s) or s[l] != s[r]:
                return

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            

            l += 1
            r -= 1
            
            if (r - l) + 1 > length:
                length = (r - l) + 1
                longest_string = s[l:r+1]


        for i in range(len(s)):
            longest(i, i)
            longest(i, i+1)
        return longest_string