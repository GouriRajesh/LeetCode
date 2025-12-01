# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Base case
        if head.next == None:
            return

        # Start with dummy node pointing to head
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy

        # Move fast pointer to nth node -> remaining nodes to traverse is (size_of_linked_list - n)
        for _ in range(n):
            fast = fast.next

        # Move slow pointer and fast pointer by 1 node each -> slow pointer will cover a distance of (size_of_linked_list - n) nodes -> slow will point to next node we want to remove
        while fast.next != None:
            fast = fast.next
            slow = slow.next

        # Delete the slow.next node by pointing it to the next node
        slow.next = slow.next.next

        return dummy.next

