class Solution:

    def binary_search_recursive(self, nums, target , i , j):
        
        # if there are no answers
        if i > j:
            return -1

        middle = (i+j)//2
        if nums[middle] == target:
            return middle
        
        if nums[middle] > target:
            return self.binary_search_recursive(nums, target, i , middle-1)            

        if nums[middle] < target:
            return self.binary_search_recursive(nums, target, middle+1, j)

    def search(self, nums: List[int], target: int) -> int:

        i = 0 # left pointer
        j = len(nums)-1 #right pointer

        # while i <= j:
        #     middle = (i+j) // 2

        #     # [4 , 5 , 6]
        #     if nums[middle] == target:
        #         # return position
        #         return middle 
        #         # return the actual number on the position
        #         # return nums[middle]

        #     # target = 4
        #     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #     if nums[middle] >  target:
        #         j = middle - 1

        #     # target = 6
        #     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #     elif nums[middle] < target:
        #         i = middle + 1

        # return -1
    
        # middle
        return self.binary_search_recursive(nums, target, i, j)