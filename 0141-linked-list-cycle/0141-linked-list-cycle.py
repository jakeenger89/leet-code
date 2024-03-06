# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        
        seen = set()
        current = head
        
        while current:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        return False
        