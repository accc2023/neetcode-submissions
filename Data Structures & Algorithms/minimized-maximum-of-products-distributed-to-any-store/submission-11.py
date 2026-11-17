class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if len(quantities) == n:
            return max(quantities)
        
        highest = max(quantities)
        total = sum(quantities)
        closest = 1000001

        left = 1
        right = highest

        def valid(curr):
            stores = 0
            for quant in quantities:
                stores += math.ceil(quant / curr)
            if stores <= n:
                return True
            else:
                return False 
        
        while left <= right:
            curr = int(left + (right - left) / 2)
            if valid(curr):
                closest = min(closest,curr)
                right = curr - 1
            else:
                left = curr + 1
        return closest
        
        
