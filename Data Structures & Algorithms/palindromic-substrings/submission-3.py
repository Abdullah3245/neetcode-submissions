class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s) - 1
        def oddPalindrome(index : int) -> int:
            if index == 0 or index == N:
                return 1
            total_palindrome = 0
            l, r = index, index

            # odd length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total_palindrome += 1
                l -= 1
                r += 1

            return total_palindrome
        
        def evenPalindrome(index: int):
            if index == N:
                return 0
            total_palindrome = 0
            l, r = index, index + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                total_palindrome += 1
                l -= 1
                r += 1

            return total_palindrome
        
        total = 0
        for i in range(N + 1):
            total += oddPalindrome(i) + evenPalindrome(i)
        
        return total
        
