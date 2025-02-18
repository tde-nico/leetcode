# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p, c = dummy, head
        
        count = 0
        while c:
            count += 1
            c = c.next
        
        while count >= k:
            c = p.next
            nxt = c.next

            for _ in range(1, k):
                c.next = nxt.next
                nxt.next = p.next
                p.next = nxt
                nxt = c.next
            
            p = c
            count -= k

        return dummy.next