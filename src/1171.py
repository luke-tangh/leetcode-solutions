# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ret = ListNode(0)
        dummy.next = head
        hashmap = {0:dummy}
        prefix_sum = 0
        
        while head:
            prefix_sum += head.val
            hashmap[prefix_sum] = head
            head = head.next
        
        head = dummy
        prefix_sum = 0

        while head:
            prefix_sum += head.val
            head.next = hashmap[prefix_sum].next
            head = head.next

        return dummy.next
