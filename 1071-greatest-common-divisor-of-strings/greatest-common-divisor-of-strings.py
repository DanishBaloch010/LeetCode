class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        merge = []
        i,j = 0,0
        if str1+str2 != str2+str1:
            return ''

        rem  = gcd(len(str1), len(str2))
        
        return str1[0:rem]

        