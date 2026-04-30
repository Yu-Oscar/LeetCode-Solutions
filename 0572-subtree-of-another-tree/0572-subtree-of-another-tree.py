# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if (not p and not q): 
                return True
            if (not p or not q): 
                return False
            if (p.val != q.val):
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right,q.right)

        def dfs(node):
            if not node:
                return False
            curr = False
            if node.val == subRoot.val:
                curr = isSameTree(node, subRoot)
            return dfs(node.left) or dfs(node.right) or curr
        return dfs(root)
            
        