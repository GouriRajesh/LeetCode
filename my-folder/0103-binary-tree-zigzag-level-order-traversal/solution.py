# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        # Start by adding root to queue
        queue = deque([root])
        # First pass is left -> right
        reverse_flag = False

        while queue:
            zz_level = []
            for _ in range(len(queue)):
                # If reverse is False, Move left -> right:
                # Pop from left
                # Append from left -> right to queue
                if reverse_flag == False:
                    node = queue.popleft()
                    zz_level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                # If reverse is True, Move right -> left:
                # Pop from right
                # Append from right -> left but to front of the queue
                elif reverse_flag == True:
                    node = queue.pop()  # Pop from end
                    zz_level.append(node.val)
                    if node.right:
                        queue.insert(0, node.right)
                    if node.left:
                        queue.insert(0, node.left)
            res.append(zz_level)
            # Flip the reverse flag at each level
            reverse_flag = not reverse_flag
        return res

