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

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let carry = 0 
    let ans = new ListNode(0)
    let curr = ans
    while (l1 && l2) {
        let sum = l1.val + l2.val + carry
        curr.val = sum % 10
        if (sum > 9) {
            carry = 1 
        } else {
            carry = 0
        }
        l1 = l1.next
        l2 = l2.next 
        if (l1 && l2) {
            curr.next = new ListNode(0)
            curr = curr.next
        }
    }

    let remain = l1 || l2
    if (carry == 0) {
        curr.next = remain
        return ans
    }

    while (remain) {
        curr.next = new ListNode(0)
        curr = curr.next
        let sum = remain.val + carry
        curr.val = sum % 10
        if (sum > 9) {
            carry = 1 
        } else {
            carry = 0
        }
        remain = remain.next
    }

    if (carry == 1) curr.next = new ListNode(1)
    

    return ans
};