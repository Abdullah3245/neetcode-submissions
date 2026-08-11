class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1, s2 = {}, {}

        for c1, c2 in zip(s, t):
            s1[c1] = s1.get(c1, 0) + 1
            s2[c2] = s2.get(c2, 0) + 1
        
        return s1 == s2