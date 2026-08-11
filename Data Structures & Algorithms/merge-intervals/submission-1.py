class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_interval = []
        merged_interval.append(intervals[0])
        for start, end in intervals[1 :]:
            last_end = merged_interval[-1][1]
            if start <= last_end:
                merged_interval[-1][1] = max(last_end, end)
            else:
                merged_interval.append([start, end])
        
        return merged_interval
        