# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return root
        def peek(stack):
            if len(stack) > 0:
                return stack[-1]
            return None
        ans=[]
        stack = []
     
        while(True):
         
            while (root):
            # Push root's right child and then root to stack
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)
 
            # Set root as root's left child
                root = root.left
         
        # Pop an item from stack and set it as root
            root = stack.pop()
 
        # If the popped item has a right child and the
        # right child is not processed yet, then make sure
        # right child is processed before root
            if (root.right is not None and
                peek(stack) == root.right):
                stack.pop() # Remove right child from stack
                stack.append(root) # Push root back to stack
                root = root.right # change root so that the
                            # right childis processed next
 
        # Else print root's data and set root as None
            else:
                ans.append(root.val)
                root = None
 
            if (len(stack) <= 0):
                break
        return ans