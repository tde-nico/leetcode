# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	def __repr__(self):
		return f'{self.val} -> {self.next}'

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = None
        while head:
            new = ListNode(head.val, new)
            head = head.next
        return new