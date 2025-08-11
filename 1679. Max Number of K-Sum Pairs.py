class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0 
        right = len(nums) - 1
        count = 0 
        nums.sort()

        while left < right:
            temp = nums[left] + nums[right] 
            if temp == k:
                count += 1
                left += 1
                right -= 1
            elif temp < k :
                left += 1
            else:
                right -= 1
                
        return count 

            
        