class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num2)):
            for j in range(len(num1)):
                digit = int(num1[j]) * int(num2[i])
                res[i + j] += digit
                res[i + j + 1] += (res[i + j] // 10)
                res[i + j] = res[i + j] % 10

        res = res[::-1]
        if res[0] == 0:
            res = res[1:]
        string_res = [str(n) for n in res]
        return "".join(string_res)
