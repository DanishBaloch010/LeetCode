class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        i = 0 
        j = len(nums)-1
        # here without = it is not working for target 0 when it is not found
        # [1,3,5,6], t = 0
        while i<=j:
            mid =(i+j)//2 
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                j = mid - 1

            if nums[mid] < target:
                i = mid + 1

        # if element is not found then it must be inserted at the left pointer+1 
        return j+1