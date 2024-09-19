class Solution:
    def isPalindrome(self, s: str) -> bool:

        # clean the string
        fil_chars = [ c.lower() for c in s if c.isalnum()]

        i , j = 0 , len(fil_chars) - 1
        
        # stop at middle, palindrom is palindrom if you check it from front to back or till the middle
        # ex: talat ,  ta l at 
        while i < j:
            if fil_chars[i] != fil_chars[j]:
                return False
            i = i + 1
            j = j - 1
                    
        return True
       


        