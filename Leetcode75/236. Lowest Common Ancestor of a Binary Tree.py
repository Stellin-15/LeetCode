# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        queue = deque([root])
        result = []
        parent={root:None}
        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.left:
                parent[node.left]=node
                queue.append(node.left)
            if node.right:
                parent[node.right]=node
                queue.append(node.right)
        anscs=set()
        while p:
            anscs.add(p)
            p=parent[p]
        while q not in anscs:
            q=parent[q]
        return q