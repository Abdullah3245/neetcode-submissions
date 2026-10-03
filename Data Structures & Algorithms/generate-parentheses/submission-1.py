class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, bracket = [], []

        def backtrack(opening, closing):
            if closing == opening == n:
                res.append("".join(bracket.copy()))
                return 

            # opening bracket
            if opening < n:
                bracket.append("(")
                backtrack(opening + 1, closing)
                bracket.pop()

            # closing bracket 
            if closing < opening:
                bracket.append(")")
                backtrack(opening, closing + 1)
                bracket.pop()

        backtrack(0, 0)

        return res