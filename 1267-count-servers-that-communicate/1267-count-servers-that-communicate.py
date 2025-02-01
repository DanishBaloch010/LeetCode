class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        r =  len(grid)
        c = len(grid[0])

        # count  = 0 
        # for i in range(r):
        #     for j in range(c):
        #         if grid[i][j] == 1:
        #             for k in range(r):
        #                 if k != i and grid[k][j] ==1:
        #                     count  = count +1
        #                     break
        #             for m in range(c):
        #                 if m != j and grid[i][m] ==1:
        #                     count  = count +1
        #                     break
        
        # return count
                        







        r =  len(grid)
        c = len(grid[0])

        row_count = [0] * r
        col_count = [0] * c

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    count = count + 1

        return count