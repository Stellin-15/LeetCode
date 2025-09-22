from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        g = defaultdict(list)
        for (a, b), k in zip(equations, values):
            g[a].append((b, k))
            g[b].append((a, 1.0/k))

        def eval_query(src, dst):
            if src not in g or dst not in g:
                return -1.0
            if src == dst:
                return 1.0
            # BFS (DFS also fine)
            q = deque([(src, 1.0)])
            seen = {src}
            while q:
                node, acc = q.popleft()
                if node == dst:
                    return acc
                for nei, w in g[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, acc * w))
            return -1.0

        return [eval_query(c, d) for c, d in queries]