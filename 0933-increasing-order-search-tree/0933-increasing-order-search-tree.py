# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(-1)  
        self.current = dummy  
        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            node.left = None
            self.current.right = node
            self.current = node
            dfs(node.right)
            

        dfs(root)
        return dummy.right
        