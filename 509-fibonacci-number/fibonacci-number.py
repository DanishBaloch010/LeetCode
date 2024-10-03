class Solution:

    # intializer constructor
    # self is used to access this memo accross the class
    def __init__(self):
        self.memo = {}

    # iterative fibonacci
    def iter_fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        prev = 0
        current = 1

        for i in range(2, n + 1):
            ans = prev + current
            prev = current
            current = ans

        return current
    
    # itterative fibonacci using list
    def itter_fib_arr(self, n):
        if n == 0 or n == 1:
            return n

        ans = [0,1]
        i = 2
        while i <= n:
            prev = ans[i-1]
            prev_prev = ans[i-2]

            ans.append(prev + prev_prev)

            i = i + 1

        return ans[-1]

    # recursive fibonacci
    def rec_fib(self, n):

        # if n == 0 or n==1:
        #     return n
        if n <= 1:
            return n
    
        return self.rec_fib(n-1) + self.rec_fib(n-2)
        
    def rec_fib_memo(self, n):
    
        if n <= 1:
            return n 

        # if previously calculated
        if n in self.memo:
            return self.memo[n]
        
        # if not previously calculated
        self.memo[n] =  self.rec_fib_memo(n-1) + self.rec_fib_memo(n-2)

        return self.memo[n]

    def fib(self, n: int) -> int:
        
        # itterative approach with variables
        # return self.iter_fib(n)

        # itterative approach with array (outplace)
        # return self.itter_fib_arr(n)

        # recursive approach without memo
        # return self.rec_fib(n)

        # recursive approach with memo
        return self.rec_fib_memo(n)