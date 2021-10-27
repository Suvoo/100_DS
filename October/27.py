# https://practice.geeksforgeeks.org/problems/concatenation-of-zig-zag-string-in-n-rows0308/1
# Ref : https://youtu.be/Q2Tw6gcVEwc

class Solution:
    def convert(self, s: str, numRows: int) -> str:
#         O(n)
        if numRows == 1:
            return s
        
        ans = ''
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r,len(s),increment):     
                ans += s[i] # for first and last row  
                if (r >  0 and r < numRows - 1) and (i + increment - 2*r < len(s)): #middle and in bounds
                    ans += s[i+increment - 2*r]
                
        return ans
        