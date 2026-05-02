class Solution(object):
    def combinationSum3(self, k, n):
        res = []

        def comb(current, k , n , start):
            if k == 0 and n == 0:
                res.append(current)
                return
            
            if k <= 0 or n <=0:
                return
            
            for i in range(start,min(10,n+1)):
                comb(current+[i],k-1,n-i,i+1)
            
        comb([],k,n,1)
        return res




# Time Complexity: O(k * C(9, k)) where C(9, k) is the number of combinations of 9 numbers taken k at a time. This is because we are generating combinations and each combination takes O(k) time to construct.
# Space Complexity: O(k) for the recursion stack and the current combination list. The result