class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right) )

import collections

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        q = collections.deque([root])
        depth = 0
        while q:
            for _ in range(len(q)):      # process one level
                node = q.popleft()
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
            depth += 1
        return depth


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        stack = [(root, 1)]
        ans = 0
        while stack:
            node, d = stack.pop()
            ans = max(ans, d)
            if node.left:  stack.append((node.left, d+1))
            if node.right: stack.append((node.right, d+1))
        return ans
