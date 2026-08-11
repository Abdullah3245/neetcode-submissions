class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case when it is not possible
        if len(s1) > len(s2):
            return False

        permutation = [0] * 26
        for c in s1:
            permutation[97 - ord(c)] += 1
        
        count = [0] * 26
        l, r = 0, len(s1) - 1

        for c in s2[:len(s1)]:
            count[97 - ord(c)] += 1

        while r < len(s2):
            if count == permutation:
                return True
            count[97 - ord(s2[l])] -= 1
            l += 1
            r += 1
            if r < len(s2):
                count[97 - ord(s2[r])] += 1
        
        return False     