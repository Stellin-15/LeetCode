# This code is for the problem "1493. Longest Subarray of 1's After Deleting One Element"
# It finds the length of the longest contiguous subarray of 1's after deleting one element
# The approach uses a sliding window technique to maintain the count of zeros in the current window
# and adjusts the start of the window when more than one zero is encountered.
# Time complexity is O(n) where n is the length of the input array.
# Space complexity is O(1) since we are using a constant amount of space.


# really good question, sliding window technique

class Solution(object):
    def longestSubarray(self, nums):
        start , end , results, zeros  = 0 , 0 , 0 , 0

        for end, num in enumerate(nums):
            if num == 0:
                zeros += 1
            
            while zeros > 1 :
                if nums[start] == 0:
                    zeros -= 1
                
                start += 1
            
            results = max(results, end - start)

        return results