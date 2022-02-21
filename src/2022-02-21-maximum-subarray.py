# https://leetcode.com/problems/maximum-subarray/


from operator import le


class Solution:
    def maxSubArray(self, nums):
        length = len(nums)
        max = nums[0]
        for i in range(length):
            sum = 0
            for j in range(length - i):
                sum += nums[i+j]
                if sum > max:
                    max = sum
        return max


assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert Solution().maxSubArray([1]) == 1
assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23


class Solution:
    def maxSubArray(self, nums):
        sum = nums[0]
        max = sum
        for n in nums[1:]:
            if sum < 0:
                if n > sum:
                    sum = n
            else:
                sum += n

            if sum > max:
                max = sum

        return max


assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert Solution().maxSubArray([1]) == 1
assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23
assert Solution().maxSubArray([-4, -2]) == -2


class Solution:
    def maxSubArray(self, nums):
        sm = 0
        maxi = nums[0]
        for i in range(len(nums)):
            sm += nums[i]

            if sm > maxi:
                maxi = sm

            if sm < 0:
                sm = 0
        return maxi


assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert Solution().maxSubArray([1]) == 1
assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23
assert Solution().maxSubArray([-4, -2]) == -2


print('done')
