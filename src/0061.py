# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        dummy = head
        prev = ListNode()
        prev.next = head
        count = 0
        while head:
            count += 1
            head = head.next
            prev = prev.next
        k = count - k%count
        for i in range(k):
            prev.next = dummy
            prev = prev.next
            dummy = dummy.next
        prev.next = None
        return dummy 