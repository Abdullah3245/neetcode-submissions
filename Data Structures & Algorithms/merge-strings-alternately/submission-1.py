class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1, s2 = len(word1), len(word2)
        merged = []

        for i in range(max(s1, s2)):
            if i < s1:
                merged.append(word1[i])
            if i < s2:
                merged.append(word2[i])

        return "".join(merged)
        