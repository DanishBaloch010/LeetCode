class Solution:
    def reverseVowels(self, s: str) -> str:
    
        # stack = []
        # vowels= 'aeiouAEIOU'

        # #capture all the vowels
        # for idx, val in enumerate(s):
        #     if val in vowels:
        #         stack.append(val)

        # # reverse the vowels and keep the other characters in same sequence.
        # ans = ''
        # for idx, val in enumerate(s):
        #     if val in vowels:
        #         ans = ans + stack.pop()
        #     else:
        #         ans = ans + val

        # return ans


            
        # class presentation
        # ans = ''
        # vowels = 'aeiouAEIOU'
        # stack = []
        # for c in s:
        #     if c in vowels:
        #         stack.append(c)

        # for c in s:
        #     if c in vowels:
        #         ans = ans + stack.pop()
        #     else:
        #         ans = ans + c

        # return ans
        
        # two pointer 
        vowels = 'aeiouAEIOU'

        s = list(s)
        i  = 0 
        j = len(s)-1

        while i < j:
            while i < j and s[i] not in vowels:
                i  = i + 1
            
            while i < j and s[j] not in vowels:
                j  = j - 1

            if i < j:
                vi = s[i]
                vj = s[j]

                s[i] = vj
                s[j] = vi 

                i = i + 1
                j = j - 1

        return ''.join(s)