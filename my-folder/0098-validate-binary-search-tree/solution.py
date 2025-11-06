# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # If no root or only 1 node
        if not root or (root.left == None and root.right == None):
            return True

        # Maintain bounds for min and max possible value initially
        minimum, maximum = [-inf, inf]

        # Recursively check if valid
        def valid(node, minimum, maximum):
            # If no node/end -> return True
            if not node:
                return True
            # Check BST condition
            if minimum < node.val and node.val < maximum:
                # Recursively check left subtree with max val as current node
                left_subtree_valid = valid(node.left, minimum, node.val)
                # Recursively check right subtree with min val as current node
                right_subtree_valid = valid(node.right, node.val, maximum)
                # If both pass BST -> Return true
                if left_subtree_valid and right_subtree_valid:
                    return True
            # BST condition fails -> Return false
            return False

        # Call on root for both left and right subtree where max(left) = min(right) = root
        return valid(root.left, minimum, root.val) and valid(
            root.right, root.val, maximum
        )

