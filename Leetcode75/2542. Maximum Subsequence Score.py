import heapq
class Solution(object):
    def maxScore(self, nums1, nums2, k):

        pairs = sorted(zip(nums1, nums2), key = lambda x: -x[1])
        heap = []
        sum_nums1 = 0
        res = 0

        for nums1, nums2 in pairs:
            heapq.heappush(heap,nums1)
            sum_nums1 += nums1

            if len(heap) > k:
                sum_nums1 -= heapq.heappop(heap)
            
            if len(heap) == k:
                res = max(res,sum_nums1 * nums2)
        
        return res
