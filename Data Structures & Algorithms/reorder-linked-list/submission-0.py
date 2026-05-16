# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow == middle 
        cur = slow
        prev = temp = None
        while(cur):
            temp = cur.next
            cur.next = prev 
            prev = cur 
            cur = temp
        
        #returns when cur = None, so end is prev 

        l = head
        r = prev
        while(l):
            tmpl = l.next 
            l.next = r
            l = tmpl

            tmpr = r.next 
            r.next = l
            r = tmpr
           