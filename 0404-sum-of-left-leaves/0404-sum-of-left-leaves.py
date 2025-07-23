# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def isLeaf(node):
            return node and not node.right and not node.left
        
        def dfs(node):
            if not node:
                return 0

            total = 0

            if isLeaf(node.left):
                total += node.left.val

            total += dfs(node.left)
            total += dfs(node.right)

            return total

        return dfs(root)