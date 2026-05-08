# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def SplitList(head):
            fast = head
            slow = head

            while fast.next:
                fast = fast.next

                if fast.next:
                    fast = fast.next
                    slow = slow.next

            sec = slow.next
            slow.next = None

            return sec

        def ReverseList(head):
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            return prev
            
        mid = SplitList(head)
        reverse = ReverseList(mid)
        curr = head

        while reverse:
            nxt = curr.next
            curr.next = reverse
            reverse = reverse.next
            curr.next.next = nxt
            curr = curr.next.next