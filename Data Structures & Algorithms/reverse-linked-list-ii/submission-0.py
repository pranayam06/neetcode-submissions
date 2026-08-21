# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l, r = None, None
        cur = dummy
        for i in range(0, right+1):
            if i == left-1:
                l = cur 
            if i == right: 
                r = cur 
            cur = cur.next 
        cur = l.next
        l_start = cur
        prev = l
        while True: 
            tmp = cur.next 
            # tmp is needed
            #cur should be r
            cur.next = prev 
            prev = cur 
            cur = tmp 
            if prev == r:
                break
        l.next = r
        l_start.next = cur
    
        return dummy.next



            
            



        
        





        