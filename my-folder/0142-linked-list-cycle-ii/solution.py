# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use a slow and fast pointer
        # Slow pointer moves by 1 and fast pointer moves by 2, if slow = fast -> cycle exists

        # Empty node or single node
        if head == None or head.next == None:
            return None

        # Both start at head
        slow = head
        fast = head

        # Move through all the nodes
        while fast and fast.next != None:
            # Move 1 node at a time
            slow = slow.next
            # Move 2 nodes at a time
            fast = fast.next.next
            # Cycle is detected
            if fast == slow:
                # Reset slow to head
                slow = head
                # Until they meet again -> implies start of cycle
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                # When slow == fast -> start of cycle
                return slow

        return None
