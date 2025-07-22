# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, mini, maxi):
            if not node:
                return True

            if not mini < node.val < maxi:
                return False

            return dfs(node.left, mini, node.val) and dfs(node.right, node.val, maxi)


        return dfs(root, float('-inf'), float('inf'))  