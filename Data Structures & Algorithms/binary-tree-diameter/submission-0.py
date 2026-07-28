# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = 0

        def helper(root: TreeNode) -> int:
            nonlocal maximum
            if root == None: return 0
            maximum = max(maximum, helper(root.left) + helper(root.right))
            return max(helper(root.left) + 1, helper(root.right) + 1)

        helper(root)
        return maximum