class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # the brute force method would be to count number of unique entities in a dictionary and then checking count > 1 in the dictionary.

        res = 0
        for num in nums:
            res = res ^ num
        return res