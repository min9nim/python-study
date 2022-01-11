# https://leetcode.com/problems/permutations

class Solution:
  def permute(self, nums):
    result = [[nums.pop()]]

    while len(nums) > 0 :
      num = nums.pop()
      new_result = []
      for i in range(len(result[0])+1) : 
        for arr in result :
          copy = arr[:]
          copy.insert(i,num)
          new_result.append(copy)
      result = new_result

    return result


s = Solution()
print(s.permute([1,2,3,4]))
