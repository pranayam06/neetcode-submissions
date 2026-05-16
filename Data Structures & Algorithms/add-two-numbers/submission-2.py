# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        f = l1
        s = l2 
        ptr = dummy = ListNode(0, None)
        carry = 0
        while (l1 and l2): 
            cur = l1.val + l2.val + carry 
            ptr.next = ListNode(cur % 10) 
            carry = cur // 10  
            l1 = l1.next 
            l2 = l2.next 
            ptr = ptr.next
        
        
        rem = l1 if l1 else (l2 if l2 else None)
        while rem: 
            cur = rem.val + carry 
            ptr.next = ListNode(cur % 10) 
            carry = cur // 10  
            rem = rem.next 
            ptr = ptr.next

        if carry: 
            ptr.next = ListNode(carry, None)
        
        return dummy.next
            

