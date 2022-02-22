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


print('done')
