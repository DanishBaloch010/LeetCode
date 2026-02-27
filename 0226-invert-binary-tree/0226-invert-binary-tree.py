# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # traverse the root in pre-order, in-order and post-order while inverting and see if it does make any difference or not.
        if root:
            # what you are about to swap with make sure you keep a copy for that in temp (nevermind, this is a just a note to myself)
            temp = root.right
            root.right =  root.left
            root.left = temp
            
            # pre-order traversal
            self.invertTree(root.left)
            self.invertTree(root.right)

        
        return root

    