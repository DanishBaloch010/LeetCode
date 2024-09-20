class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0:
            return True
        i  = 0
        while i < len(flowerbed):
            
            # check if place is empty
            if flowerbed[i] == 0 :
                # check if its the first place or the previous place is empty
                prev_flower = (i==0)  or (flowerbed[i-1] == 0)
                # check if its the last place or the next place is empty
                next_flower = (i==len(flowerbed)-1) or (flowerbed[i+1] == 0)
                
                # there is a zero and both places are empty then plant the flower
                if prev_flower and next_flower:
                    flowerbed[i] = 1
                    n = n - 1
                
                    # if all flowers are planted after checks then return True
                    if n == 0:
                        return True
            
            i = i + 1
    
        print(n)
        # else all flowers are not planted hence return False
        return False
        