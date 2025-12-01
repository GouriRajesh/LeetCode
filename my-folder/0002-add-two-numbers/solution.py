# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Keep a dummy node and then skip it in the end
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            if sum >= 10:
                carry = sum // 10
                sum = sum % 10
            else:
                carry = 0
            new_node = ListNode(val=sum)
            curr.next = new_node
            curr = new_node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

