import numpy as np
class Solution:
    def hammingWeight(self, n: int) -> int:

        binary =  ""

        while n > 0:
            binary = str(n%2) + binary
            n = n // 2
            
        print(binary)
        count = 0
        for bit in binary:
            if bit == '1':
                count= count + 1

        return count



        
        
        