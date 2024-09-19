class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i, j = 0 , len(numbers)-1

        while True:
            # if target found then return
            if numbers[i] + numbers[j] ==  target:
                return [i +1 , j +1]
            # if sum is greater become closer from left side to find a lesser number
            if numbers[i] + numbers[j] > target:
                j = j - 1
            # otherwise move forward from right side to find a bigger number 
            else:
                i = i + 1



            