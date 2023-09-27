# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        tdummy = tail = prev = ListNode()
        hdummy = head
        while head and head.next:
            tail.next = ListNode(head.next.val)
            tail = tail.next
            head.next = head.next.next
            prev = head
            head = head.next
        if not head:
            if not prev:
                return ListNode()
            prev.next = tdummy.next
        elif not head.next:
            head.next = tdummy.next
        else:
            tail.next = head
            head = head.next
            head.next = tdummy.next
        return hdummy
