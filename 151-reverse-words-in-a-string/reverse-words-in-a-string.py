class Solution:

    def split_words(self, s:str) -> list:
        all_words = []
        cur_word = []

        for c in s:
            if c != ' ':
                cur_word.append(c)
            else:
                if cur_word:
                    all_words.append(''.join(cur_word))
                    cur_word = []

        if cur_word:
            all_words.append(''.join(cur_word))

        return all_words
    


    def reverseWords(self, s: str) -> str:
        
        # custom function
        # s_split = self.split_words(s)

        # built in function
        s_split = s.split()

        print(s_split)
        ans = []
        i = len(s_split)-1
        while i >= 0:

            ans.append(s_split[i])
            i = i - 1
        
        return ' '.join(ans)






        

        
        