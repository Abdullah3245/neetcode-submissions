class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        s1 = len(word1)
        s2 = len(word2)
        merged = []
        alt = True

        while i < s1 and j < s2:
            if alt:
                merged.append(word1[i])
                i += 1
                alt = False
            else:
                merged.append(word2[j])
                j += 1
                alt = True
        
        if i < s1:
            merged.append(word1[i:])
        
        if j < s2:
            merged.append(word2[j:])
        
        return "".join(merged)
        