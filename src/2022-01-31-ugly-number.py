
class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        while True:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                return n == 1


assert Solution().isUgly(6) == True
assert Solution().isUgly(1) == True
assert Solution().isUgly(14) == False
assert Solution().isUgly(0) == False

# 시간복잡도는 log(N)

print('done')
