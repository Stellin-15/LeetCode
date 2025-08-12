class Solution(object):
    def longestOnes(self, nums, k):
        max_window_length = 0
        num_zeros = 0 
        n = len(nums)
        left = 0

        for right in range(n):
            if nums[right] == 0:
                num_zeros += 1
            
            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1

            window = right - left + 1
            max_window_length = max(max_window_length,window)

        return max_window_length