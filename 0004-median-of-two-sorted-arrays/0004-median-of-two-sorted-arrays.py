class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr = []
        for i in nums1:
            arr.append(i)
        for i in nums2:
            arr.append(i)

        arr.sort()
        if len(arr)%2==0:
            index = len(arr)//2

            ans = (arr[index] + arr[index-1])/2
            return ans
        else:
            index = len(arr)//2
            return arr[index]
