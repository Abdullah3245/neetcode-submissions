class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = defaultdict(int)
        l, r = 0, len(s) - 1
        for i, c in enumerate(s):
            chars[c] = i
        
        res = []
        size = end = 0
        for i,c in enumerate(s):
            size += 1
            end = max(end, chars[c])
            if i == end:
                res.append(size)
                size = 0

        return res


