class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # first = float("inf")
        # second = float("inf")
        first = nums[0]
        second = nums[1]
        for idx, val in enumerate(nums):
            if val <= first:
                first = val
            elif val <= second:
                second = val
            else:
                return True
        return False
