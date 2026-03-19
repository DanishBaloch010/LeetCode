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

        total_num_of_nodes = 0
        while queue:

            # queue holds the current level of tree, to check the level boundry we count the length of the current state of queue.
            print(f"level boundry : {len(queue)}")
            # traverse the tree level wise.
            for i in range(len(queue)):
                node = queue.popleft()
                # counting each non-null node. (adding towards total number of codes.)
                total_num_of_nodes = total_num_of_nodes +1 

                print(node.val)
                if node.left:
                    queue.append(node.left)
                    print(node.left.val)

                if node.right:
                    queue.append(node.right)
                    print(node.right.val)

            print("-" *70)

            depth = depth + 1
        
        print(f"total depth : {depth}")
        print(f"total number of nodes : {total_num_of_nodes}")

        return depth        