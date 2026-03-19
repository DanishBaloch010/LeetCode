# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        depth =  0

        q = deque([root])

        while q:
            # if we are returning in the middle of the loop then we have to update the depth first to show the current level of tree. this is to ensure to avoid any kind of miscalculations.
            depth = depth +1
            for i in range(len(q)):

                n = q.popleft()

                if not n.left and not n.right:
                    return depth
                
                if n.left:
                    q.append(n.left)

                if n.right:
                    q.append(n.right)

        return depth 


        