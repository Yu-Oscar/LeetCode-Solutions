# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visited = {}
        while curr:
            if curr in visited:
                return True
            visited[curr] = True
            curr = curr.next
        return False