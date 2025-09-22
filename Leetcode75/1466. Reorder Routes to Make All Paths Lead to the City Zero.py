class Solution(object):
    def minReorder(self, n, connections):
        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append((b, 1))  # original direction a -> b (away from 0 if we traverse from a)
            adj[b].append((a, 0))  # opposite view b -> a (toward 0)

        def dfs(u, parent):
            changes = 0
            for v, needs_reverse in adj[u]:
                if v == parent:
                    continue
                changes += needs_reverse
                changes += dfs(v, u)
            return changes

        return dfs(0, -1)
        