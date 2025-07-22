# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right 

        def invert(node):
            if not node:
                return 
            
            invert(node.left)
            invert(node.right)

            left = node.left
            right = node.right
            
            node.right = left
            node.left = right 

        def same(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            return same(node1.left, node2.right) and same(node1.right, node2.left)
        
        return same(left, right)
        