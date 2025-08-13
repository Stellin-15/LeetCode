class Solution(object):
    def largestAltitude(self, gain):
        max_height = 0
        current_height = 0 

        for i in range(len(gain)):
            current_height = current_height + gain[i]
            max_height = max(max_height,current_height)


        return max_height



