# Recursive
class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        if root is None:
            return
        
        root.left,root.right = root.right,root.left
        
        if root.left is not None:
            self.mirror(root.left)
        if root.right is not None:
            self.mirror(root.right)