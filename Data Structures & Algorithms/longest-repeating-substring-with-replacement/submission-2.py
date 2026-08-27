class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique = {}
        l, r = 0, 1
        unique[s[l]] = unique.get(s[l], 0) + 1
        longest = 1
        N = len(s)

        while r < N:
            curr = s[r]
            unique[curr] = unique.get(s[r], 0) + 1 
            max_frequency = max(unique.values())
            replacements = (r - l + 1) - max_frequency 
            if replacements > k:
                while l < N and replacements > k:
                    unique[s[l]] -= 1
                    if unique[s[l]] == 0:
                        unique.pop(s[l])
                    l += 1
                    max_frequency = max(unique.values())
                    replacements = (r - l + 1) - max_frequency 
                
            longest = max(longest, r - l + 1)
            r += 1
        return longest