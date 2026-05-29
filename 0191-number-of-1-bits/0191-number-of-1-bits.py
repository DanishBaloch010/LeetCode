class Solution:
    def hammingWeight(self, n: int) -> int:

        set_bits = 0 
        while n:
            # add when right most bit & operation is 1 or 0, zero will have no effect on the addition.
            set_bits += n & 1
            # shift the bits from left to right.
            n = n >> 1

        return set_bits 
        