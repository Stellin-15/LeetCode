class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        area = 0 

        while left < right:
            width = right - left
            length = min(height[right],height[left])
            area = max(area,width * length)

            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        
        return area 


