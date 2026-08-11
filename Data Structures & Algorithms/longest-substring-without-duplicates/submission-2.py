class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest_substring = 0
        unique = set()
        l, r = 0, 0
        while r < n:
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            if s[r] not in unique:
                unique.add(s[r])
                r += 1
            longest_substring = max(longest_substring, r - l)
        return longest_substring

        return longest_substring