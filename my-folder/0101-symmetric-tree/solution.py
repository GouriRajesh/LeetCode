# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        leftroot = root.left
        rightroot = root.right

        def checkSame(leftroot, rightroot):
            if leftroot == None and rightroot == None:
                return True
            if leftroot == None or rightroot == None:
                return False
            return (
                leftroot.val == rightroot.val
                and checkSame(leftroot.left, rightroot.right)
                and checkSame(leftroot.right, rightroot.left)
            )

        result = checkSame(leftroot, rightroot)
        return result

