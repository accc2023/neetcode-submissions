# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        min_heap = []

        queue = []
        if root: queue.append(root)
        while queue:
            size = len(queue)
            level_sum = 0
            while size > 0:
                curr = queue.pop(0)
                level_sum += curr.val
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
                size -= 1
            print(level_sum)
            min_heap.append(level_sum)

        min_heap = [-i for i in min_heap]
        heapq.heapify(min_heap)
        if k > len(min_heap): return -1
        # print(min_heap)
        while min_heap and k > 1:
            heapq.heappop(min_heap)
            k -= 1
        # print(min_heap)
        return -min_heap[0]
