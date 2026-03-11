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

/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
    let fast = head 
    let slow = head 
    while (fast && fast.next) {
        slow = slow.next
        fast = fast.next.next
    }

    let curr = slow.next
    slow.next = null

    let prev = null
    while (curr) {
        let next = curr.next
        curr.next = prev
        prev = curr 
        curr = next
    }
    curr = head 
    while (curr && prev) {
        let next1 = curr.next
        let next2 = prev.next
        curr.next = prev
        prev.next = next1
        curr = next1
        prev = next2
    }
};