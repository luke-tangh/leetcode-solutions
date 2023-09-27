# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        root = dummy = ListNode()
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r) -> ListNode():
        dummy = root = ListNode()
        while l and r:
            if l.val < r.val:
                root.next = l
                l = l.next
            else:
                root.next = r
                r = r.next
            root = root.next
        root.next = l or r
        return dummy.next
