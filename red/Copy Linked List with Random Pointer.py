
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr=head
        x={None:None}
        while curr:
            x[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            x[curr].next=x[curr.next]
            x[curr].random=x[curr.random]
            curr=curr.next
        return x[head]
