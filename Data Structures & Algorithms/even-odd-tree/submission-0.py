# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = []
        if root: queue.append(root)
        level = 0
        while queue:
            size = len(queue)
            recent = 0
            if level % 2 == 0: 
                recent = -1 
            else: 
                recent = 1000001
            while size > 0:
                curr = queue.pop(0)
                if level % 2 == 0 and (curr.val % 2 == 0 or recent >= curr.val):
                    return False
                if level % 2 != 0 and (curr.val % 2 != 0 or recent <= curr.val):
                    return False
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                recent = curr.val
                size -= 1
            level += 1
        return True
