class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # this is the naive recursive approach to solve this problem 

        # Nevermind, notes to myself: first return what the functions wants
        # then think about the smallest possible solution that you would like to solve and find the base case around them most probably the termination cases of the algorithm.

        # each operation cost is 1.
        def compute(i, j):
            
            if (i,j) in memo:
                return memo[(i,j)]

            # these base cases are only hit once so there is no need to store them.
            if i == len(word1) and j == len(word2):
                # we have exhausted the search from the both strings thus there is no operation cost attached to it.
                return 0

            if i == len(word1) and j < len(word2):
                return (1 * (len(word2)-j))

            if i < len(word1) and j == len(word2):
                return (1 * (len(word1) -i)) 

            # this conditional check should be below base cases to prevent out of index error, because the above conditions prevents the pointer going out of bound.
            if word1[i] == word2[j]:
                # before returning the answer store it in the memo and then check it at the top of this function to see if the solution for particular i and j already exists.
                memo[(i,j)] = compute(i+1,j+1)
                return memo[(i,j)]
            
            cost_insert = 1 + compute(i , j+1)
            cost_del = 1 + compute(i+1, j)
            cost_replace = 1 + compute(i+1 , j+1)

            memo[(i,j)] = min(cost_insert,cost_del,cost_replace)
            return memo[(i,j)]
        
        memo = {}
        return compute(0,0)