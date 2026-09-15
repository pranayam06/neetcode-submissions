# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy.next 
        while (cur and cur.next): 
            a = cur 
            b = cur.next 
            a.next = ListNode(math.gcd(a.val, b.val), b)
            cur = b 
        return dummy.next
