class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        best = float('-inf')
        ans, lvl = 1, 1
        while q:
            s = 0
            nq = []
            for u in q:
                s += u.val
                if u.left:
                    nq.append(u.left)
                if u.right:
                    nq.append(u.right)
            if s > best:
                best = s
                ans = lvl
            q = nq
            lvl += 1
        return ans