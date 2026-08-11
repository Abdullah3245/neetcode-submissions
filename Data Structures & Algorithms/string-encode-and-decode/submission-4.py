class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            length = len(s)
            encoded = encoded + str(length) + '#' + s
        print(encoded)
        return encoded        

    def decode(self, s: str) -> List[str]:
        decoded = ""
        length = len(s)
        index = 0
        l = []
        while index < length:
            j = index
            while s[j] != '#':
                j += 1
            size = int(s[index:j])
            l.append(s[j + 1: j + 1 + size])
            index = j + size + 1
        return l
