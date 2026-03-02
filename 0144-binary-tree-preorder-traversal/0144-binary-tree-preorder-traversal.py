# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        q = []

        if root:

            # q.append(root.val)
            
            # q.append(root.left.val)
            # q.append(root.right.val)

            # this does not work because it returns the "nodes" classes i guess, but have to re-verify (right now ,sleepy)
            # q.append(self.preorderTraversal(root.left))
            # q.append(self.preorderTraversal(root.right))
            
            # q.extend(self.preorderTraversal(root.left))
            # q.extend(self.preorderTraversal(root.right))

            # single line pythonic way of doiing it, wrap the first element in [] because the next calls return the list.
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


        return q