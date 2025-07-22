# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        table = defaultdict(int)
        max_count = [0]
        ans = []
        def dfs(node):
            if not node:
                return 

            table[node.val] += 1
            
            if table[node.val] > max_count[0]:
                max_count[0] = table[node.val]
                ans.clear()
                ans.append(node.val)
            elif table[node.val] == max_count[0]:
                ans.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans
            
        