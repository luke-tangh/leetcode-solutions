# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        dummy = ListNode()
        dummy.next = head
        while head and head.next:
            dummy_next = dummy.next
            temp = head.next
            dummy.next, head.next, temp.next = temp, temp.next, dummy_next
        return dummy.next
    