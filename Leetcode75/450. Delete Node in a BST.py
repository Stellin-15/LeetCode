class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root



class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            # no child 
            if not root.left and not root.right:
                return None
            # one child 
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # two child 
            else:
            # find inorder successor (min of right subtree)
                succ = root.right
                while succ.left:
                    succ = succ.left
                root.val = succ.val
            # delete that successor
            root.right = self.deleteNode(root.right,succ.val)
        return root