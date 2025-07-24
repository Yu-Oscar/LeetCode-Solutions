# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans1 = []
        ans2 = []
        def dfs(node ,ls):
            if not node:
                return 
            
            if not node.left and not node.right:
                ls.append(node.val)

            dfs(node.right, ls)
            dfs(node.left, ls)

        dfs(root1, ans1)
        dfs(root2, ans2)
        return ans1 == ans2