class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        seen = set()

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in seen:
                    seen.add(j)
                    dfs(j)

        provinces = 0
        for i in range(n):
            if i not in seen:
                provinces += 1
                seen.add(i)
                dfs(i)
        return provinces