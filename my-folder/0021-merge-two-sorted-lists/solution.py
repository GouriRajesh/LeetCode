# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Handle Base Cases
        if not list1 and not list2:
            return
        if not list1:
            return list2
        if not list2:
            return list1

        # Store the head with the smallest value for the result list
        # Here list1 is list with smaller start value
        if list1.val < list2.val:
            res_head = list1
            l1 = list1
            l2 = list2
        # Here list2 is list with smaller start value
        else:
            res_head = list2
            l1 = list2
            l2 = list1
        # By now l1 is list with smaller start value and l2 with greater start value

        while l1 and l2:
            while l1 and l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            # Change the linkage
            temp.next = l2
            # Swap l1 and l2 when l1 becomes greater-> always make l1 the list with smaller value
            swapper = l1
            l1 = l2
            l2 = swapper

        return res_head

