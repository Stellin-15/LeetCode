class Solution(object):
    def longestZigZag(self, root):

        self.ans = 0

        def dfs(node):
            if not node:
                return (-1,-1)

            l_left,l_right = dfs(node.left)
            r_left,r_right = dfs(node.right)

            left_len = 1 + l_right 
            right_len = 1 + r_left

            self.ans = max(self.ans,left_len,right_len)
            return(left_len,right_len)
        


        dfs(root)
        return self.ans
    
    
    
class Solution(object):
    def longestZigZag(self, root):

        self.count = 0

        def dfs(node,left,right):

            self.count = max(self.count,left,right)

            if node.left:
                dfs(node.left,right+1,0)
            if node.right:
                dfs(node.right,0,left+1)

        dfs(root,0,0)
        return self.count