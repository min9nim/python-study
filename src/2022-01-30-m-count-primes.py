# https://leetcode.com/problems/count-primes/

import math
from tkinter import S


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        if n == 3:
            return 1
        if n == 4:
            return 2

        primes = [3]

        for num in range(5, n, 2):
            isPrime = True
            sr = math.sqrt(num)
            for p in primes:
                if p > sr:
                    break
                if num % p == 0:
                    isPrime = False
                    break
            if isPrime:
                print(num)
                primes.append(num)

        return len(primes) + 1


# assert Solution().countPrimes(0) == 0
# assert Solution().countPrimes(1) == 0
# assert Solution().countPrimes(2) == 0
# assert Solution().countPrimes(3) == 1
# assert Solution().countPrimes(4) == 2
# assert Solution().countPrimes(5) == 2
# assert Solution().countPrimes(6) == 3
# assert Solution().countPrimes(7) == 3
# assert Solution().countPrimes(8) == 4


class Solution2:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [2]
        nums = list(range(3, n, 2))

        while nums:
            primes.append(nums[0])
            nums = [x for x in nums if x % primes[-1] != 0]
            print(primes[-1], len(nums))

        return len(primes)


# assert Solution2().countPrimes(0) == 0
# assert Solution2().countPrimes(1) == 0
# assert Solution2().countPrimes(2) == 0
# assert Solution2().countPrimes(3) == 1
# assert Solution2().countPrimes(4) == 2
# assert Solution2().countPrimes(5) == 2
# assert Solution2().countPrimes(6) == 3
# assert Solution2().countPrimes(7) == 3
# assert Solution2().countPrimes(8) == 4
# Solution2().countPrimes(1000000)


class Solution3:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = []
        m = dict()
        for num in range(2, n):
            m[num] = True

        while m:
            primes.append(list(m.keys())[0])
            print('primes', primes)
            del m[primes[-1]]
            for i in range(primes[-1] * primes[-1], n, primes[-1]):
                if i in m:
                    del m[i]

        return len(primes)


# assert Solution2().countPrimes(0) == 0
# assert Solution2().countPrimes(1) == 0
# assert Solution2().countPrimes(2) == 0
# assert Solution2().countPrimes(3) == 1
# assert Solution2().countPrimes(4) == 2
# assert Solution2().countPrimes(5) == 2
# assert Solution2().countPrimes(6) == 3
# assert Solution2().countPrimes(7) == 3
# assert Solution2().countPrimes(8) == 4


class Solution4:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [2]
        m = dict()
        for num in range(3, n, 2):
            m[num] = True

        while m:
            p = next(iter(m))
            pp = p*p
            primes.append(p)
            del m[p]
            if pp > n:
                break
            for i in range(pp, n, p):
                if i in m:
                    del m[i]

        print(primes + list(m.keys()))
        return len(primes) + len(m)


Solution4().countPrimes(10)


print('done')

# Ref) https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html
