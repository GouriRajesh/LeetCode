# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Empty node
        if not head:
            return head
        # 1 node
        if head.next == None:
            head = None
            return head
        # 2 nodes
        if head.next.next == None:
            head.next = None
            return head

        # Start from the head
        slow = head
        fast = head

        # Traverse till last node
        while fast and fast.next != None:
            # Move 1 node
            slow = slow.next
            # Move 2 node
            fast = fast.next.next

        # Get the middle node
        mid = slow
        # Set the value of middle node to be the next node's value
        mid.val = mid.next.val
        # Set the next of middle node to be the next node's next pointer -> "deleting" the middle node by copying next node it to the middle
        mid.next = mid.next.next

        return head
