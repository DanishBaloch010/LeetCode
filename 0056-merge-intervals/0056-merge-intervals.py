class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort the interval first based on the start value so that we know that they are line up in sequential increasing order based in start.
        sorted_intervals_on_start = sorted(intervals , key = lambda x: x[0])
        prev_interval = [sorted_intervals_on_start[0]]

        for idx, next_interval in enumerate(sorted_intervals_on_start , start =1):

                # if next interval start is smaller than or equals to the previous interval end then it means the next one inside the previous one
                if next_interval[0] <= prev_interval[-1][1]:
                    # update the max outer boundry
                    prev_interval[-1][1] =  max(prev_interval[-1][1] , next_interval[1])

                else:
                    prev_interval.append(next_interval)

        return prev_interval
                
            




        