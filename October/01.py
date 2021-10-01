
# https://practice.geeksforgeeks.org/problems/check-for-bst/1#
# CHECK 2nd approach too

class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    arr = []
    def inorder(self,node):
        if node is None:
            return 
        self.inorder(node.left)
        self.arr.append(node.data)
        self.inorder(node.right)
        
    def isBST(self, root):
        #code here
            
        self.inorder(root)
        print(self.arr)
        for i in range(1,len(self.arr)):
            if self.arr[i] <= self.arr[i-1]:
                return False
        return True