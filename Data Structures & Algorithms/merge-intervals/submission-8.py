class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item: item[0])

        merged_intervals = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = merged_intervals[-1][1]
            if lastEnd >= start:
                end = max(merged_intervals[-1][1], end)
                merged_intervals[-1][1] = end
            else:
                merged_intervals.append([start, end])
        

        return merged_intervals
