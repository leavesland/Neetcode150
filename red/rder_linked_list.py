# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        middle=second
        prev = None
        while middle:
            nxt=middle.next
            middle.next=prev
            prev=middle
            middle=nxt
        while prev:
            fn=head.next
            sn=prev.next
            head.next=prev
            head.next.next=fn
            head=fn
            prev=sn
        
