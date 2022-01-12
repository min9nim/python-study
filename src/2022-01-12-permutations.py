# https://leetcode.com/problems/permutations

class Solution:
  def permute(self, nums):
    result = [[nums.pop()]]

    for num in nums :
      new_result = []
      for i in range(len(result[0])+1) : 
        for arr in result :
          copy = arr[:]
          copy.insert(i,num)
          new_result.append(copy)
      result = new_result

    return result


class Solution2:
    def permute(self, nums):
        res=[]
        n=len(nums)
        
        def go(l,r):
            if l==r:
                res.append(nums.copy())
                return 
            for i in range(l,r+1):
                nums[l],nums[i]=nums[i],nums[l]
                go(l+1,r)
                nums[l],nums[i]=nums[i],nums[l]
            
        go(0,n-1)
        return res 



s = Solution2()
print(s.permute([1,2]))