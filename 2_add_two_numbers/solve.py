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
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		l3 = ListNode()
		curr = l3
		c = 0
		while l1 or l2 or c:
			curr.next = ListNode()
			curr = curr.next
			v1 = l1.val if l1 else 0
			v2 = l2.val if l2 else 0
			v = v1 + v2 + c
			curr.val = v % 10
			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None
			c = v // 10
		return l3.next