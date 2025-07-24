# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x_parent = self.y_parent = None
        self.x_depth = self.y_depth = -1
        def dfs(node, step, parent):
            if not node:
                return 

            if x == node.val:
                self.x_parent = parent
                self.x_depth = step

            if y == node.val:
                self.y_parent = parent
                self.y_depth = step

            dfs(node.left, step+1, node)
            dfs(node.right, step+1, node)
        
        dfs(root, 0, None)
        return (self.x_depth == self.y_depth) and (self.x_parent != self.y_parent)