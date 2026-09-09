# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currl1=l1
        currl2=l2
        listl1=[]
        listl2=[]
        listl3=[]
        num1=0
        num2=0
        while currl1 is not None:
            listl1.append(currl1.val)
            currl1=currl1.next
        while currl2 is not None:
            listl2.append(currl2.val)
            currl2=currl2.next
        for i in range(len(listl1)):
            num1+=listl1[i]*(10**i)
        for i in range(len(listl2)):
            num2+=listl2[i]*(10**i)
        final_sum=num1+num2
        x=len(str(final_sum))
        y=str(final_sum)
        for i in range(x-1,-1,-1):
            listl3.append(y[i])
        answer=ListNode(0,None)
        temp=answer
        for i in range(len(listl3)):
            n = ListNode(listl3[i],None)
            temp.next = n
            temp=temp.next
        return answer.next
    def addTwoNumbersBetter(self, l1, l2):
        dummy = ListNode(0)
        curr=dummy
        carry = 0
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            total=l1+l2+carry
            carry=total//10
            curr.next=ListNode(total%10)
            curr=curr.next
            l1=l1.next if l1.next else None
            l2=l2.next if l2.next else None
        return dummy.next
