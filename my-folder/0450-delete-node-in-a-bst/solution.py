# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return root

        parent = None
        curr = root

        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            elif key > curr.val:
                curr = curr.right
        if not curr:
            return root

        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            if not parent:
                return child
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
            
        else:
            par = None
            to_del = curr
            curr = curr.right
            while curr.left:
                par = curr
                curr = curr.left
            if par != None:
                par.left = curr.right
                curr.right = to_del.right
            curr.left = to_del.left

            if not parent:
                return curr
            if parent.left == to_del:
                parent.left = curr
            else:
                parent.right = curr

        return root

