from collections import deque
class Solution(object):
    def maxLevelSum(self, root):
        if not root:
            return 0
        
        q = deque([root])
        best_level = 1
        level = 1
        max_sum = float('-inf')

        while q:
            level_sum = 0 
            for i in range(len(q)):
                node = q.popleft()
                level_sum += node.val 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum 
                best_level = level 
            level += 1

        return best_level