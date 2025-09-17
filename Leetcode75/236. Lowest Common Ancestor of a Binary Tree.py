class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root 
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right

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