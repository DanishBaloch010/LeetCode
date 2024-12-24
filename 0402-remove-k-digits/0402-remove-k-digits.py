class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Result list to store the smallest number
        result = []
        
        for digit in num:
            # Remove larger digits from the result if k > 0
            while result and k > 0 and result[-1] > digit:
                result.pop()
                k -= 1
            result.append(digit)
        
        # Remove remaining digits if k > 0
        result = result[:-k] if k > 0 else result
        
        # Convert the result back to a string and strip leading zeros
        return "".join(result).lstrip('0') or "0"




