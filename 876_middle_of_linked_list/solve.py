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
	def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if head.next is None:
			return head
		start = head
		end = head.next
		while end:
			end = end.next
			start = start.next
			if not end:
				break
			end = end.next
		return start
            
            
        