# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # Hash set solution = Time: O(m+n), Space: O(m)
        # node_set = set()
        # while headA:
        #     if headA not in node_set:
        #         node_set.add(headA)
        #         headA = headA.next

        # while headB:
        #     if headB in node_set:
        #         return headB
        #     headB = headB.next

        # return None

        # Two Pointer Solution = Time: O(m+n), Space: O(1)
        # Main Tip: Make both list length's the same by switching to other -> Move together and compare node

        if not headA or not headB:
            return None

        a, b = headA, headB

        # Traverse both lists -> switch to other head when reaching end
        # If the lists intersect, the pointers will eventually meet at the intersection -> if not, both become None at the same time and return None.
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a

