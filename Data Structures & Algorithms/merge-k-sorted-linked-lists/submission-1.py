# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.nxt = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i))
        res = ListNode()
        res_ptr = res

        while heap:
            cur, idx = heapq.heappop(heap)
            node = lists[idx] 
            res_ptr.next = node 
            res_ptr = res_ptr.next
            lists[idx] = node.next 
            if lists[idx]: 
                heapq.heappush(heap, (lists[idx].val, idx))  
        return res.next
        
        




        

