class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort intervals by start time -> increasing order
        intervals.sort()
        res = []
        # Set first interval to compare with the next
        compare = intervals[0]

        for i in intervals:
            start = i[0]
            end = i[1]
            # Overlap exists
            if start <= compare[1]:
                # Prev start and max btw prev end and current end
                compare = [compare[0], max(compare[1], end)]
            else:
                # No overlap, add to result
                res.append(compare)
                compare = [start, end]

        # Add last interval to result
        res.append(compare)
        return res

