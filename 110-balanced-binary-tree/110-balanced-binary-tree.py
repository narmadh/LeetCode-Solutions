# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root)!=-1
    def height(self,root):
        if root==None:
            return 0
        else:
            lDepth=self.height(root.left)
            if lDepth==-1:
                return -1
            rDepth=self.height(root.right)
            if rDepth==-1:
                return -1
            if(abs(lDepth - rDepth) > 1):
                return -1  
            return max(lDepth,rDepth)+1
        
        