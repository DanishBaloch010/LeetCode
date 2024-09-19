class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        small = nums[0]
        for idx, val in enumerate(nums):
            if abs(val) < abs(small):
                small = val

        # if the number is negative and also the positive version of it is present in the array.
        if small < 0 and abs(small) in nums:
            # return positive
            return abs(small)
        else:
            # return negative
            return small