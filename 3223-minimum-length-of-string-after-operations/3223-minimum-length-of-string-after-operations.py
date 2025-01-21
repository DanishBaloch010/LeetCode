class Solution:
    def minimumLength(self, s: str) -> int:
        
        counts = Counter(s)

        ans = 0
        for c in counts.values():
            # if count is even then their will be chars left in the end
            if c % 2 == 0:
                ans = ans + 2
            # if count is odd then there will be one char left in the end
            else:
                ans = ans + 1
            
        return ans

