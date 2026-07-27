/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        Collections.sort(intervals, (a, b) -> Integer.compare(a.start, b.start));
        if (intervals.isEmpty()) return 0;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        int max = 1;
        minHeap.offer(intervals.get(0).end);
        for (int i = 1; i < intervals.size(); i++) {
            while (!minHeap.isEmpty() && intervals.get(i).start >= minHeap.peek()) {
                minHeap.poll();
            }
            minHeap.offer(intervals.get(i).end);
            max = Math.max(max, minHeap.size());
        }
        return max;
    }
}
