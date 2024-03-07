# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        middle = head
        secondmiddle = head
        
        while secondmiddle and secondmiddle.next:
            middle = middle.next
            secondmiddle = secondmiddle.next.next
        
        return middle