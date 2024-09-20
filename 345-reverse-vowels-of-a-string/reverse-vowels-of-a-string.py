class Solution:
    def reverseVowels(self, s: str) -> str:
    
        stack = []
        vowels= 'aeiouAEIOU'

        #capture all the vowels
        for idx, val in enumerate(s):
            if val in vowels:
                stack.append(val)

        # reverse the vowels and keep the other characters in same sequence.
        ans = ''
        for idx, val in enumerate(s):
            if val in vowels:
                ans = ans + stack.pop()
            else:
                ans = ans + val

        return ans


            



