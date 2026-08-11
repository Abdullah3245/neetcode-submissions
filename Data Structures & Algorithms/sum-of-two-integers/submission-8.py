class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while (b != 0):
                temp = ((a & b) << 1) & mask
                a = (a ^ b) & mask 
                b = temp
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
        
        