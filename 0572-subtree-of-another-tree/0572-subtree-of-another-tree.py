# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.ans = False
        def same(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            return same(node1.left, node2.left) and same(node1.right, node2.right)


        def dfs(node):
            if not node:
                return 

            if node.val == subRoot.val and same(node, subRoot):
                self.ans = True 
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ans        