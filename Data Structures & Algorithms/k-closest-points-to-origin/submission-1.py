class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(max_heap,(-dist,point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [element[1] for element in max_heap]
        