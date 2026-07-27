class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        rightsum = 0
        for i in range(0, len(nums)):
            rightsum = total - leftsum - nums[i]
            if rightsum == leftsum:
                return i
            leftsum += nums[i]

        return -1