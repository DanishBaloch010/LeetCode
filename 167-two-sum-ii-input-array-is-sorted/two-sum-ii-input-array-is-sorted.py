class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i, j = 0 , len(numbers)-1

        while True:
            if numbers[i] + numbers[j] ==  target:
                return [i +1 , j +1]
            if numbers[i] + numbers[j] > target:
                j = j - 1
            else:
                i = i + 1



            