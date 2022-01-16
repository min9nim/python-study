# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums, target):
      dic = {}
      for i in range(len(nums)) :
        if nums[i] in dic :
          return [dic[nums[i]], i]
        else :
          dic[target - nums[i]] = i
        


s = Solution()
print(s.twoSum([2,7,11,15], 9))