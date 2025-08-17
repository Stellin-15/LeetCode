class Solution(object):
    def increasingTriplet(self, nums):
        FN = float("inf")
        SN = float("inf")

        for n in nums:
            if n <= FN:
                FN = n
            elif n<= SN:
                SN = n 
            else:
                return True
        
        return False

        
        