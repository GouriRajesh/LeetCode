# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Empty node or single node
        if not head or head.next == None:
            return head

        # Set a tail pointer for later
        tail = head
        # Count number of nodes
        n = 1
        # Loop to count number of nodes and set tail
        while tail.next != None:
            tail = tail.next
            n += 1

        # If k is a multiple of length of ll -> return head as it is
        if k % n == 0:
            return head

        # Move to n-kth node and update links
        curr = head
        # How many "actual" rotations
        new_k = k % n
        for _ in range(n - new_k - 1):
            curr = curr.next
        # Set the tail's next to be head
        tail.next = head
        # New head is the next node of current
        head = curr.next
        # Set current next to be Null
        curr.next = None
        # Set current as the new tail
        tail = curr

        return head

