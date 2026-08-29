class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        added = False

        for start, end  in intervals:
            # interval alreay added
            if added:
                merged.append([start, end])
            # overlap so just merge for now 
            elif start <= newInterval[1] and newInterval[0] <= end:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
            # new interval less than the curr interval so add both in order
            elif newInterval[1] <= start:
                merged.append(newInterval)
                merged.append([start, end])
                added = True
            # no overlap
            else:
                merged.append([start, end])
        
        if not added:
            merged.append(newInterval)
        return merged
                