class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        result = 0

        while left <= right:

            mid = (left + right) // 2

            if self.hours(piles,mid) <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result

    
    def hours(self, piles, mid):
        hours = 0 
        for p in piles:
            hours += (p + mid - 1) // mid
        
        return hours
# Time Complexity: O(n log m) where n is the number of piles and m is the maximum number of bananas in a pile.
# Space Complexity: O(1) since we are using only a constant amount of extra space


