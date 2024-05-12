class Solution(object):
    def searchRange(self, nums, target):
        if target in nums:
             for i in range(len(nums)):
                   if target == nums[i]:
                        return [i,i]
                   elif target < nums[i]:
                        return [nums.index(target),nums.index(target)+1]
        else:
                return ([-1,-1])
            
print(Solution().searchRange([1,2,3],2))