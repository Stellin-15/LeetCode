import heapq
class SmallestInfiniteSet(object):

    def __init__(self):
        self.curr = 1
        self.added_back = []
        self.added_back_set = set()
        

    def popSmallest(self):

        if self.added_back:
            smallest = heapq.heappop(self.added_back)
            self.added_back_set.remove(smallest)
            return smallest
        
        val = self.curr
        self.curr += 1 
        return val 

        

    def addBack(self, num):
        if num < self.curr and num not in self.added_back_set:
            heapq.heappush(self.added_back, num)
            self.added_back_set.add(num)

        


