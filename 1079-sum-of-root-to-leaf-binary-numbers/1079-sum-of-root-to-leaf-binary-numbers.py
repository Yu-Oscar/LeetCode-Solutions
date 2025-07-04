# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def dfs(node, curr_val):
            if not node:
                return 0
            
            curr_val = (curr_val << 1) | node.val

            if not node.left and not node.right:
                return curr_val

            return dfs(node.left, curr_val) + dfs(node.right, curr_val)
        
        return dfs(root, 0)