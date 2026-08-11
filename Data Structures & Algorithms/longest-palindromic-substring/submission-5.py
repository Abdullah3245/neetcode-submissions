class Solution:
        def longestPalindrome(self, s: str) -> str:
            n = len(s)
            longest_palindrome = s[0]
            for i in range(0, n):
                # odd palindrome
                l, r = i, i
                while l >= 0 and r < n and s[l] == s[r]:
                    if (r - l + 1) > len(longest_palindrome):
                        longest_palindrome = s[l:r + 1]
                    l -= 1
                    r += 1
                
                # even palindrome
                l, r = i, i + 1
                while l >= 0 and r < n and s[l] == s[r]:
                    if (r - l + 1) > len(longest_palindrome):
                        longest_palindrome = s[l:r + 1]
                    l -= 1
                    r += 1
            
            return longest_palindrome