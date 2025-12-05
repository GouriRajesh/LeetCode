# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # ---- Works but time limit exceeded
        # curr = head

        # def reverse(node):
        #     if not node:
        #         return
        #     prev = None
        #     curr = node
        #     while curr:
        #         temp = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = temp

        #     return prev

        # while curr:
        #     curr.next = reverse(curr.next)
        #     curr = curr.next

        # return head

        # ------Move to mid, reverse second half of ll
        # Move 2 pointer simultaneously, from start and from mid after reversing
        # Merge 2 pointers together

        slow, fast = head, head

        # 1. Find middle node
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # Found mid node -> send second half for reversing
        mid = slow.next

        # Break list
        slow.next = None

        # 2. Reverse from mid
        prev = None
        curr = mid

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Mid value is now prev
        mid = prev

        # 3. Move start and mid together and take one after the other
        start = head
        while mid:
            temp1 = start.next
            temp2 = mid.next

            start.next = mid
            mid.next = temp1

            start = temp1
            mid = temp2

