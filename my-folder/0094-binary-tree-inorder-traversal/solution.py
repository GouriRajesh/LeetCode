# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# ----- RECURSIVE SOLUTION -----
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         traversal_result = []
#         if root == []:
#             return []

#         def traverse(node):
#             if not node:
#                 return
#             traverse(node.left)
#             traversal_result.append(node.val)
#             traverse(node.right)

#         traverse(root)
#         return traversal_result


# ----- ITERATIVE SOLUTION -----
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        if root == []:
            return []

        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result

