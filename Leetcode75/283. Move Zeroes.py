class Solution(object):
    def moveZeroes(self, nums):
        count = len(nums)
        j = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for i in range(j,count):
            nums[i] = 0 
