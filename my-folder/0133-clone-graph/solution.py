"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # Idea: BFS

        if not node:
            return

        # Keep track of old nodes
        q = deque([node])
        # New copied nodes
        oldToNew = {node: Node(node.val, [])}

        # While old nodes to copy
        while q:
            curr_node = q.popleft()
            # Current copied node
            copy_node = oldToNew[curr_node]

            # For all neighbors in current node to copy
            for neighbor in curr_node.neighbors:
                # If neighbour's node is not yet copied
                if neighbor not in oldToNew:
                    # Copy it
                    oldToNew[neighbor] = Node(neighbor.val)
                    # Add orig neighbour to queue
                    q.append(neighbor)
                # Update new copied node's neighbours to be the new neighbor created
                copy_node.neighbors.append(oldToNew[neighbor])

        # Return the root of the copied nodes
        return oldToNew[node]

