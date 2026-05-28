class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        unique = {}
        for n in nums:
            if n in unique:
                unique[n] += 1
            else:
                unique[n] = 1

        for key, value in unique.items():
            if value > 1:
                return True
    
        return False

