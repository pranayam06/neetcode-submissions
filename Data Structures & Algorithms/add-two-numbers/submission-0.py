# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ta = l1 
        tb = l2 
        carry = 0
        res = output = ListNode()
        output.val = 0
         
        while ta or tb or carry:   
            if not ta: 
                ta = ListNode(0)
            
            if not tb: 
                tb = ListNode(0) 
            
            print((ta.val + tb.val + carry) % 10)

            output.next = ListNode((ta.val + tb.val + carry) % 10 ) 
            print(output.next.val)
            carry = (ta.val + tb.val + carry) // 10

            ta = ta.next 
            tb = tb.next    
            output = output.next
        
        return res.next
            

            

            