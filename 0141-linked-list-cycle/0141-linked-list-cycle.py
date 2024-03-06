# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        
        behind = head
        ahead = head.next
        
        while ahead and ahead.next:
            if behind == ahead:
                return True
            behind = behind.next
            ahead = ahead.next.next
            
        return False
        
        
        