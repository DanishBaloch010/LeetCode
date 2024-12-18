class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")
        for idx, val in enumerate(nums):
            if val <= first:
                first = val
            elif val <= second:
                second = val
            else:
                return True
        return False