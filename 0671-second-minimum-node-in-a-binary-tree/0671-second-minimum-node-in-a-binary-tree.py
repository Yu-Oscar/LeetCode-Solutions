# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            #base case(leaf)
            if not node.left:
                return -1

            left_val = node.left.val
            right_val = node.right.val

            if left_val == node.val:
                left_val = dfs(node.left)
            
            if right_val == node.val:
                right_val = dfs(node.right)

            if left_val == -1:
                return right_val
            if right_val == -1:
                return left_val
            
            return min(left_val, right_val)

        return dfs(root)
        