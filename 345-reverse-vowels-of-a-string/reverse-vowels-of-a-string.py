class Solution:
    def reverseVowels(self, s: str) -> str:
    
        stack = []
        vowels= 'aeiouAEIOU'

        for idx, val in enumerate(s):
            if val in vowels:
                stack.append(val)
        
        ans = ''
        for idx, val in enumerate(s):
            if val in vowels:
                ans = ans + stack.pop()
            else:
                ans = ans + val

        return ans


            



