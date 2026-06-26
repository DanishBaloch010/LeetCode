class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        sorted_intervals =  sorted(intervals, key=lambda x: x[0])

        print(sorted_intervals)

        results = [sorted_intervals[0]]
        for idx, next_interval in enumerate(sorted_intervals, start=1):
            prev_interval = results[-1]
            # if the start of the next is under the previous one then merge them.
            if next_interval[0] <= prev_interval[1]:
                # store the start and the end
                results[-1][1] =  max(prev_interval[1], next_interval[1])
            # no overlap, means the interval is distinct
            else:
                results.append(next_interval)


        return results







        return [1,2]
        