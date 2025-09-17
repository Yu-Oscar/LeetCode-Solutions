"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
            
        def dfs(node):
            if not node:
                return 0
            curr = 0
            for child in node.children:
                curr = max(curr, 1 + dfs(child))

            return curr

        return 1 + dfs(root)