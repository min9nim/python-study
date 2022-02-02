# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            numIncluded = []
            for arr in result:
                numIncluded.append(arr + [num])
            result += numIncluded
        return result

# 시간복잡도: O(N*2^N)
# 공간복잡도: O(N*2^N)


print(Solution().subsets([1, 2, 3]))
