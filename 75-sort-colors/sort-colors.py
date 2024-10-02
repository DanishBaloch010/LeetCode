class Solution:
    def three_pointers_dutch_flag(self, nums):

        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # return self.three_pointers_dutch_flag(nums)

        # counting sort
        count = [0, 0, 0]

        for num in nums:
            count[num] += 1
        
        print(count)
        
        index = 0
        
        for color in range(len(count)):
            for _ in range(count[color]):
                nums[index] = color
                index += 1