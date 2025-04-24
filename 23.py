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
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		new = ListNode()
		res = new
		while list1 or list2:
			if (list1 and not list2) or (list1 and list1.val <= list2.val):
				new.next = ListNode(list1.val)
				new = new.next
				list1 = list1.next
			else:
				new.next = ListNode(list2.val)
				new = new.next
				list2 = list2.next
		return res.next

	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		if not lists:
			return None
		if len(lists) == 1:
			return lists[0]
		mid = len(lists) // 2
		l1 = self.mergeKLists(lists[:mid])
		l2 = self.mergeKLists(lists[mid:])
		return self.mergeTwoLists(l1, l2)
