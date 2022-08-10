# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root==None:
            return 0
        else:
            lDepth=self.height(root.left)
            rDepth=self.height(root.right)
            if lDepth>rDepth:
                return lDepth+1
            else:
                return rDepth+1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            lh=self.height(root.left)
            rh=self.height(root.right)
            if(abs(lh-rh))>1:
                return False
            left=self.isBalanced(root.left)
            right=self.isBalanced(root.right)
            if(left==False or right==False):
                return False
        return True
            