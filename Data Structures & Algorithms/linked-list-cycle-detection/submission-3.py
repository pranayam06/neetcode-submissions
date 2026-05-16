# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: 
        slow = head  
        if not head.next:
            return False
        fast = head.next
         

        while slow!=fast:  
            if not fast.next or not fast.next.next: 
                return False 
            slow = slow.next
            fast = fast.next 
            fast = fast.next
        
        return True

            
        