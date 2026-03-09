"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h = { None: None }
        
        c = head
        while c:
            h[c] = Node(c.val)
            c = c.next
        
        c = head
        while c:
            cp = h[c]
            cp.next = h[c.next]
            cp.random = h[c.random]
            c = c.next

        return h[head]
