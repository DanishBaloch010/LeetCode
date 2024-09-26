class Solution:
    def search(self, nums: List[int], target: int) -> int:

        i = 0 # left pointer
        j = len(nums)-1 #right pointer


        while i <= j:
            middle = (i+j) // 2

            # [4 , 5 , 6]
            if nums[middle] == target:
                # return position
                return middle 
                # return the actual number on the position
                # return nums[middle]

            # target = 4
            # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            if nums[middle] >  target:
                j = middle - 1

            # target = 6
            # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            elif nums[middle] < target:
                i = middle + 1

        return -1
        