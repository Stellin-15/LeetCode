class Solution:
    def swimInWater(self, g: List[List[int]]) -> int:
        def bfs(t):
            seen,q = {(0,0)},[(0,0)]*(g[0][0]<=t)
            while q and (len(g)-1,)*2 not in q:
                seen.update(q:={(ii,jj) for i,j in q for ii,jj in ((i+1,j),(i,j+1),(i-1,j),(i,j-1))
                    if 0<=ii<len(g)>jj>=0 and g[ii][jj]<=t and (ii,jj) not in seen})
            return (len(g)-1,)*2 in q

        return bisect_left(range(max(chain(*g))),1,key=bfs)