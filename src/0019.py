# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        def remove(head, n):            
            if head == None:
                return head, 0
            node, count = remove(head.next, n)
            count += 1
            head.next = node
            if count == n:
                head = head.next
            return head, count
        return remove(head, n)[0]
