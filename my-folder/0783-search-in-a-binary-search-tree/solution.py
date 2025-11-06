# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If node is empty or None -> return None
        if not root:
            return None
        # If node val == val -> Return node
        if root.val == val:
            return root
        else:
            # If val < node val -> Move to left subtree and check again
            if val < root.val:
                return self.searchBST(root.left, val)
            # If val > node val -> Move to right subtree and check again
            elif val > root.val:
                return self.searchBST(root.right, val)
        
