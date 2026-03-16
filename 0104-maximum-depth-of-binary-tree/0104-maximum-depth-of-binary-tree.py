# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # this is BFS level order traversal.
        depth = 0
        if not root:
            return 0

        queue = deque([root])

        while queue:

            # traverse the entire level
            for i in range(len(queue)):
                node = queue.popleft()

                print(node.val)
                if node.left:
                    queue.append(node.left)
                    print(node.left.val)

                if node.right:
                    queue.append(node.right)
                    print(node.right.val)
            print("-" *70)

            depth = depth + 1

        return depth        