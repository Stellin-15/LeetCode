class Solution(object):
    def reverse(self, x):
        sign = 1 if x >= 0 else -1

        x = abs(x)
        output = 0
        while x:
            output = output * 10 + (x % 10)
            x = x/10
        
        if output > 2**31 - 1:
            return 0
        
        return sign * output