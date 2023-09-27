# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = head
        while head and head.next:
            temp = head.next.val
            head.next.val = head.val
            head.val = temp
            head = head.next.next
        return dummy
    