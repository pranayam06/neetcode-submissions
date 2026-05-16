# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = []
        for i in range(len(lists)):
            if lists[i]:
                heads.append([lists[i].val, i])

        heapq.heapify(heads)

        dummy = ListNode()
        cur = dummy
        while heads:
            val, i = heapq.heappop(heads)
            cur.next = lists[i]
            lists[i] = lists[i].next 
            if lists[i]:
                heapq.heappush(heads, [lists[i].val, i])
            cur = cur.next 
        
        return dummy.next



