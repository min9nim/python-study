# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        isPositive = n > 0

        if not isPositive:
            n = -n

        result = x
        for _ in range(n-1):
            result *= x

        if isPositive:
            return result
        else:
            return 1 / result


assert Solution().myPow(2.00000, 10) == 1024.00000


class Solution:
    def __init__(self):
        self.map = dict()

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n in self.map:
            return self.map[n]

        isPositive = n > 0
        if not isPositive:
            n = -n

        n1 = n // 2
        n2 = n - n1

        result = self.myPow(x, n1) * self.myPow(x, n2)

        if isPositive:
            self.map[n] = result
            return result
        else:
            return 1 / result


assert Solution().myPow(2.00000, 10) == 1024.00000
assert Solution().myPow(2.10000, 3) == 9.261000000000001

print('done')
