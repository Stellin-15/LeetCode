import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        total = 0

        left_heap, right_heap = [], []
        l, r = 0, n - 1

        # initial fill
        while l < candidates and l <= r:
            heapq.heappush(left_heap, (costs[l], l))
            l += 1
        while r >= n - candidates and r >= l:
            heapq.heappush(right_heap, (costs[r], r))
            r -= 1

        for _ in range(k):
            # pick cheapest between left and right
            if right_heap and (not left_heap or right_heap[0][0] < left_heap[0][0] or
                               (right_heap[0][0] == left_heap[0][0] and right_heap[0][1] < left_heap[0][1])):
                cost, idx = heapq.heappop(right_heap)
                total += cost
                if r >= l:  # refill right
                    heapq.heappush(right_heap, (costs[r], r))
                    r -= 1
            else:
                cost, idx = heapq.heappop(left_heap)
                total += cost
                if l <= r:  # refill left
                    heapq.heappush(left_heap, (costs[l], l))
                    l += 1

        return total


