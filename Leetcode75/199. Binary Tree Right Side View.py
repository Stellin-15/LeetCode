class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = deque()
        q.append(root)

        while q:
            right_side = None

            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
            
            if right_side:
                res.append(right_side.val)
        
        return res
    
    
    
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()

                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return result