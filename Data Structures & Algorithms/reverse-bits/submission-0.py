class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            curr_bit = (n >> i) & 1
            res = res | (curr_bit << (31 - i))
        return res