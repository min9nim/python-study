# https://leetcode.com/problems/perfect-number/
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        dividers = []
        for n in range(2, math.floor(math.sqrt(num))+1):
            if num % n == 0:
                dividers.append(n)
                dividers.append(num // n)

        sum = 0
        for n in dividers:
            sum += n

        return sum + 1 == num


assert Solution().checkPerfectNumber(28) == True
assert Solution().checkPerfectNumber(7) == False


print('done')
