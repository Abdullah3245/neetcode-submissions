class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        characters = set()
        start = 0

        for index, c in enumerate(s):
            if c in characters:
                while c in characters:
                    characters.remove(s[start])
                    start += 1
            characters.add(c)
            length = max(length, len(characters))

        return length
            