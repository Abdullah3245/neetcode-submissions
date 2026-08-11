class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        sorted_interval = [intervals[0]]
        index = 0
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if sorted_interval[index][1] > curr[0]:
                sorted_interval[index][1] = min(curr[1], sorted_interval[index][1])
            else:
                sorted_interval.append(curr)
                index += 1
        print(sorted_interval)
        return len(intervals) - len(sorted_interval)       