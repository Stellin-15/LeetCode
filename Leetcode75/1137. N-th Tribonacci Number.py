class Solution(object):
    def tribonacci(self, n):
        arr = [0,1,1]

        if n < 3:
            return arr[n]
        
        for i in range(3, n+1):
            arr[0], arr[1], arr[2] = arr[1] , arr[2] , sum(arr)
        
        return arr[2]
# Time Complexity: O(n)
# Space Complexity: O(1)