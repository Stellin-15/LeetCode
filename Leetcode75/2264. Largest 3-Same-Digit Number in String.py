class Solution(object):
    def largestGoodInteger(self, num):
        best = ''

        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                if best == '' or num[i] > best:
                    best = num[i]

        return best *3 if best else "" 
