# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []

        result = []
        q = deque([root])
        
        while q:
            level_size = len(q)
            level_node = []

            for _ in range(level_size):
                node = q.popleft()
                level_node.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            result.append(level_node)
        return result

                

            
        