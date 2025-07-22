# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return True, 0
            
            left_balanced, left_h = dfs(node.left)
            if not left_balanced:
                return False, 0

            right_balanced, right_h = dfs(node.right)
            if not right_balanced:
                return False, 0

            return abs(left_h-right_h) <= 1, (1 + max(left_h, right_h))

        return dfs(root)[0]       