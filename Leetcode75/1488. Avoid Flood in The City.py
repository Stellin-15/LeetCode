import heapq
from collections import defaultdict

def avoidFlood(rains):
    n = len(rains)
    ans = [-1] * n
    next_rains = defaultdict(list)

    # Step 1: record all rain days for each lake
    for i, lake in enumerate(rains):
        if lake > 0:
            next_rains[lake].append(i)

    filled = set()
    heap = []  # (next_rain_day, lake)

    for i, lake in enumerate(rains):
        if lake > 0:
            # Remove current day from queue
            next_rains[lake].pop(0)

            # Flood check
            if lake in filled:
                return []
            filled.add(lake)

            # If it rains again later, push the next day to heap
            if next_rains[lake]:
                heapq.heappush(heap, (next_rains[lake][0], lake))

            ans[i] = -1

        else:  # dry day
            if heap:
                next_day, dry_lake = heapq.heappop(heap)
                filled.remove(dry_lake)
                ans[i] = dry_lake
            else:
                ans[i] = 1  # arbitrary
    return ans