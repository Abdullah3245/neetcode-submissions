class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occurrences = {}
        res = 0
        l, r = 0, 0
        for character in s:
            occurrences[character] = occurrences.get(character, 0) + 1
            while r - l + 1 - max(occurrences.values()) > k:
                occurrences[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res        