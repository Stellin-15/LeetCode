
class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None 
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


class Solution(object):
    def searchBST(self, root, val):
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return None