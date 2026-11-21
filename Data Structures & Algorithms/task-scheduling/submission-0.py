class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        for task in tasks:
            if task not in hashmap:
                hashmap[task] = 1
            else:
                hashmap[task] += 1
        max_heap = []
        for key,val in hashmap.items():
            heapq.heappush(max_heap, (-val, key))
        queue = deque()
        time = 0
        while max_heap or queue:
            if max_heap: 
                curr = heapq.heappop(max_heap)
                curr = (curr[0] + 1, curr[1]) # process most freq task available
                if curr[0] != 0: queue.append((curr, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
            time += 1

        return time