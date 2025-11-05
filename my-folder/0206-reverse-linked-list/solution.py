# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start with the last pointer which is None
        prev = None
        # Begin with head
        curr = head

        # Move from left -> right until None
        while curr:
            # Store next node
            temp = curr.next
            # Update current pointer to prev node
            curr.next = prev
            # Move the prev pointer to current node
            prev = curr
            # Move current pointer to next node
            curr = temp

        # Return the first pointer (curr is None here as it has reached the end)
        return prev

