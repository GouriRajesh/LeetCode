# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # # Option: 1
        # # Using a set to keep track of the nodes visited -> store the node and not the values
        # visited = set()
        # curr = head
        # # Traverse all the nodes
        # while curr != None:
        #     # Check if the node is already visited previously
        #     if curr in visited:
        #         return True
        #     # Else mark it as visited by adding to the set
        #     visited.add(curr)
        #     # Move to the next node
        #     curr = curr.next

        # return False

        # Option 2:
        # Using slow ans fast pointers -> slow moves 1 at a time and fast moves 2 at a time
        # If cycle exists slow will meet fast else fast reaches the end of the ll

        # Empty or Single Node
        if head == None or head.next == None:
            return False

        # Both start at head
        slow = head
        fast = head
        print(fast.val)

        # Traverse through all nodes
        while fast and fast.next != None:
            # Move 1 node at a time
            slow = slow.next
            # Move 2 nodes at a time
            fast = fast.next.next
            # Check if slow and fast point to same node -> cycle exists
            if slow == fast:
                return True

        return False

