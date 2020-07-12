# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode()
        curnode = prehead
        while l1  and l2:
            if l1.val < l2.val:
                curnode.next = l1
                l1 = l1.next
            else:
                curnode.next = l2
                l2 = l2.next
            curnode=curnode.next
        curnode.next = l1 if l1 else l2
        return  prehead.next