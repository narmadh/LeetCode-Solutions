# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        queue=[root]
        wrapList=[[root.val]]
        while queue:
            subList=[]
            queueLength=len(queue)
            for i in range(queueLength):
                node=queue[0]
                del queue[0]
                if node.left:
                    queue.append(node.left)
                    subList.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    subList.append(node.right.val)
            if subList:
                wrapList.append(subList)
        return wrapList