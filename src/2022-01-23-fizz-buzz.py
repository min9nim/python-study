# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int):
        r3 = n % 3
        r5 = n % 5

        if r3 == 0 and r5 == 0:
            return 'FizzBuzz'
        elif r3 == 0:
            return 'Fizz'
        elif r5 == 0:
            return 'Buzz'
        else:
            return str(n)


print('success!')
