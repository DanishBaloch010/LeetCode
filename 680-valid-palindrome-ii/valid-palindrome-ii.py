class Solution:

    # def validPalindrome(self, s: str) -> bool:

    def validPalindrome(self, s): # S is a string
        left=0
        right=len(s)-1
        s1=""
        s2=""
        # iterative approach (x)
        while left<=right:
            if s[left]!=s[right]:
                # first element ko nahi lega
                # first element ko lega?
                s1=s[:left]+s[left+1:]
                # last element ko nahi lega
                s2=s[:right]+s[right+1:]
                return s1==s1[::-1] or s2==s2[::-1]
            left+=1
            right-=1
        return True
                