class Solution:
    def minSwaps(self, s: str) -> int:
        closing = 0
        max_closing = float('-inf')

        for c in s:
            if c == '[':
                closing -= 1
            if c == ']':
                closing += 1
            max_closing = max(max_closing, closing)
        
        return (max_closing + 1) // 2