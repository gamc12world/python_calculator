class Solution(object):
    def searchInsert(self, nums, target):
        nums.sort()
        x1=[num for num in nums]
        if target in x1:
                return print(x1.index(target)) 
        else:
            nums.append(target)
            nums.sort()
            x4=[num for num in nums]
            if target in x4:
                return print(x4.index(target))

Solution().searchInsert([1,3,5,6],5)