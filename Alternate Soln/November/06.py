# repeated substraction but TLE.

class Solution:
    def divide(self, a, b):
        #code here
        ans = 0
        while a>=b:
            a = a - b
            ans+=1
        return ans
