# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Optional Parameters means that the parameters can hold value or can be None

        temp1 = l1
        temp2 = l2
        nextvalue = 0

        head = None
        temp = head

        # Check if both lists contain value
        while temp1 is not None and temp2 is not None:
            sum = temp1.val + temp2.val + nextvalue
            nextvalue = sum // 10
            currentvalue = sum % 10

            if temp is None:
                new_node = ListNode(currentvalue)
                head = new_node
                temp = new_node
            else:
                new_node = ListNode(currentvalue)
                temp.next = new_node
                temp = new_node

            temp1 = temp1.next
            temp2 = temp2.next

        while temp1 is not None:
            sum = temp1.val + nextvalue
            nextvalue = sum // 10
            currentvalue = sum % 10

            new_node = ListNode(currentvalue)
            temp.next = new_node
            temp = new_node
            temp1 = temp1.next

        while temp2 is not None:
            sum = temp2.val + nextvalue
            nextvalue = sum // 10
            currentvalue = sum % 10

            new_node = ListNode(currentvalue)
            temp.next = new_node
            temp = new_node
            temp2 = temp2.next

        if nextvalue != 0:
            new_node = ListNode(nextvalue)
            temp.next = new_node
            temp = new_node

        return head

