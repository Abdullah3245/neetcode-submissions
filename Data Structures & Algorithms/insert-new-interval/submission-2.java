class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> merged = new ArrayList<>();
        //edge cases
        if (intervals.length == 0) {
            int[][] empty = new int[1][1];
            empty[0] = newInterval;
            return empty;
        }
        int[] first = intervals[0];
        if (first[0] > newInterval[1]) {
            // adding the new internal to the start and we are done
            merged.add(newInterval);
            for (int[] interval : intervals) {
                merged.add(interval);
            }
            return merged.toArray(new int[merged.size()][]);
        }
        int i = 0;
        int n = intervals.length;
        // 1. Add intervals that come before the new interval
        while (i < n && intervals[i][1] < newInterval[0]) {
            merged.add(intervals[i]);
            i++;
        }

        // 2. Merge overlapping intervals
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        merged.add(newInterval); // Add the merged interval

        // 3. Add the remaining intervals
        while (i < n) {
            merged.add(intervals[i]);
            i++;
        }

        return merged.toArray(new int[merged.size()][]);

    }
}
