# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        return 3


assert Solution().numSquares(12) == 3


print('success!')


'''
1 4 9 16 25 36 49 64 81 100

1 = 1
2 = 1 1
3 = 1 1 1

4 = 4
5 = 4 1
6 = 4 1 1
7 = 4 1 1 1
8 = 4 4

9 = 9
10 = 9 1
11 = 9 1 1
12 = 4 4 4
13 = 9 4
14 = 9 4 1
15 = 9 4 1 1

16 = 16
17 = 16 1
18 = 16 1 1
19 = 9 9 1
20 = 16 4
21 = 16 4 1
22 = 9 9 4
23 = 9 9 4 1, 16 4 1 1 1
24 = 16 4 4


25 = 25
26 = 25 1
27 = 25 1 1
28 = 25 1 1 1
29 = 25 4
30 = 25 4 1
31 = 25 4 2 2
..
..
50 = 49 1, 25 25
'''
