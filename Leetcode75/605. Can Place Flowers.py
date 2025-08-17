class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0: return True

        i = 0
        count = len(flowerbed)

        while i < count:
            if flowerbed[i] == 0:
                prev = 0 if i == 0 else flowerbed[i-1]
                nex = 0 if i == count - 1 else flowerbed[i+1]
                if prev == 0 and nex == 0:
                    flowerbed[i] = 1
                    n-=1
                    if n == 0:
                        return True
                    i+=2
                    continue 
            i+=1
        return False
            

        