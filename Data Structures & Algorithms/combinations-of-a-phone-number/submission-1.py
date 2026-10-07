class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, combination = [], []

        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i):
            if i >= len(digits):
                res.append("".join(combination[:]))
                return 
            
            curr = digits[i]
            for c in mapping[curr]:
                 combination.append(c)
                 backtrack(i + 1)
                 combination.pop()
        
        backtrack(0)
        return res

