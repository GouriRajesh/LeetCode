"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        # If root is None, return it
        if not root:
            return

        # BFS (Level-order traversal)
        res = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                # Append node directly, not the value
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Append None to the end of each level nodes
            level.append(None)
            res.append(level)

        # From the level-order traversal list, link them contiguously together
        for level in res:
            # Stop before reaching None
            for i in range(len(level) - 1):
                node = level[i]
                node.next = level[i + 1]

        return root

