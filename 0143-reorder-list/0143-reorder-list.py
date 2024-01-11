# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle, fast and slow pointer
        slow, fast= head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #reverse second half
        start=slow.next
        prev=slow.next = None
        while start:
            temp=start.next
            start.next=prev
            prev=start
            start=temp
            
        #merge second to first half every other
        first, second= head, prev
        while second:
            temp1, temp2=first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2