# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node, curr):
            if not node:
                return 
            
            curr.append(node.val)

            if not node.left and not node.right:
                ans.append('->'.join(map(str, curr)))
                return 
            
            
            dfs(node.left, curr.copy())
            dfs(node.right, curr.copy())

        dfs(root, [])
        return ans


        