# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        from collections import defaultdict

        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # empty path

        def dfs(node, curr):
            if not node:
                return 0

            curr += node.val
            # number of paths ending at this node with sum == targetSum
            res = prefix_count[curr - targetSum]

            # include current prefix
            prefix_count[curr] += 1

            # explore
            res += dfs(node.left, curr)
            res += dfs(node.right, curr)

            # backtrack
            prefix_count[curr] -= 1
            return res

        return dfs(root, 0)
