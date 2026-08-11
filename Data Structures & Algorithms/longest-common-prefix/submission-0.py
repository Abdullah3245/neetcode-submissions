class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        length = len(strs[0])
        for i in range(0, length):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix