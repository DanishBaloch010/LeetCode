class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        greatest = candies[0]

        for idx, val in enumerate(candies):
            if val > greatest:
                greatest = val
        
        res=[]

        for idx, val in enumerate(candies):
            if val + extraCandies >= greatest:
                res.append(True)
            else:
                res.append(False)
        
        return res

        