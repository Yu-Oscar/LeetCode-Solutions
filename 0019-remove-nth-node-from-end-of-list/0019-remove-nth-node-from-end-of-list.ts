/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let front = head
    let end = head
    for (let i = 0; i < n; i++) {
        end = end.next
    }
    if (end == null) return head.next

    while (end && end.next) {
        front = front.next
        end = end.next
    }

    front.next = front.next.next
    return head
};