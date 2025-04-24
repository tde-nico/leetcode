# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = ListNode(0, head)
        slow = tmp

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            slow = slow.next

        slow.next = slow.next.next

        return tmp.next
        