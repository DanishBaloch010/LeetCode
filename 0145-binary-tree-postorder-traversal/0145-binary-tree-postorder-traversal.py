# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        q = []

        q.extend(self.postorderTraversal(root.left))
        q.extend(self.postorderTraversal(root.right))

        q.append(root.val)

        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

        return q
        