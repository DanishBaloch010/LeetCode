class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        i = 0 
        j = len(nums)-1
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