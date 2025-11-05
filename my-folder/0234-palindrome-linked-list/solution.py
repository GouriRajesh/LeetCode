# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Option 1: Convert to list and check from from and compare with back
        # Option 2: Traverse LL add to stack. Traverse list again and check with popped element
        # Option 3: Reverse from middle of LL and traverse together to check equality

        # Empty node or single node
        if head == None or head.next == None:
            return True

        # Define the reverse function
        def reverse(node):
            prev = None
            curr = node

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        # Start from head
        slow = head
        fast = head

        # Till you reach last node -> slow gives middle value
        while fast and fast.next != None:
            # Move 1 node
            slow = slow.next
            # Move 2 node
            fast = fast.next.next

        # Reverse the ll at mid position
        mid = reverse(slow)

        # Traverse together from head and from mid
        curr = head
        while mid:
            if curr.val != mid.val:
                return False
            curr = curr.next
            mid = mid.next
        return True

