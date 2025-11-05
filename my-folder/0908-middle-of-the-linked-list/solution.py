# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Single node -> Return it
        if head.next == None:
            return head

        # Slow pointer
        slow_temp = head
        # Fast pointer
        fast_temp = head

        # While fast pointer is not None and next is also not None
        while fast_temp and fast_temp.next != None:
            # Fast pointer moves by 2 places
            fast_temp = fast_temp.next.next
            # Slow pointer moves by 1 place
            slow_temp = slow_temp.next

        # When we reach the end of the array -> return the middle
        return slow_temp

