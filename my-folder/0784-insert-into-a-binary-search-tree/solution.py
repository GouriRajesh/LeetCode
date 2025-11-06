# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Create new node
        new_node = TreeNode(val, left=None, right=None)
        # If tree is empty
        if root == None:
            return new_node

        # If tree not empty
        # If val is less that current root value -> Move to left subtree
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # If val is greater that current root value -> Move to right subtree
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root

