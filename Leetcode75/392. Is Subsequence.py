class Solution(object):
    def isSubsequence(self, s, t):
        n = len(s)
        m = len(t)
        i , j = 0 , 0 

        if n == 0:
            return True
        if m == 0 or n > m:
            return False
        
        while i < n and j < m:
            if s[i] == t[j]:
                i +=1 
            
            j +=1
        
        
        return i == len(s)

