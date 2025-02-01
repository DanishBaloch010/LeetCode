class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        # bad solution
        # i = 0 
        # j = 1

        # if len(nums) == 1:
        #     return True
        # check = False
        # while i < len(nums) and j < len(nums)-1:
            
        #     if (nums[i] % 2 == 0 and nums[j] % 2 != 0) or (nums[i] % 2 != 0 and nums[j] % 2 == 0):
        #         check = True
        #     else:
        #         check = False

        #     i = i +1
        #     j = j + 1
        
        # return check

        # good solution

        for i in range(len(nums) -1):
            # means adjacent values are of same parity
            if (nums[i]%2 == nums[i+1]%2):
                return False
        
        return True
