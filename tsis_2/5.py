class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        su = 0
        pr = 1
        s = str(n)

        for i in range(len(s)):
            pr *= int(s[i])
            su += int(s[i])


        return pr - su
