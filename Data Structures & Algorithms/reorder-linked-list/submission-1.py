# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left = head
        
        while left.next and left.next.next:
            temp = left.next
            right = left.next
            prev = None
            while right.next:
                prev = right
                right = right.next
            if prev: prev.next = None
            left.next = right
            left = left.next
            left.next = temp
            left = left.next
        