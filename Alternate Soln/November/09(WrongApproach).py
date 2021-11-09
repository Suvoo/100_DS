# Taking Maxsum

from collections import Counter
class Solution:
    def RulingPair(self, arr, n): 
        # Your code goes here
        def findSum(n):
            s = list(str(n))
            s = [int(i) for i in s]
            su = sum(s)
            return su
        
        su = []
        for i in arr:
            su.append(findSum(i))
        # print(su)
        dicc = Counter(su)
        mxsum = 0
        for i in dicc :
            # print(i,dicc[i])
            if dicc[i] >= 2:
                mxsum = max(mxsum,i)
        # print(mxsum)
        
        ans = []
        for i in range(len(arr)):
            if su[i] == mxsum:
                ans.append(arr[i])
        # print(ans)
        if len(ans) == 0:
            return (-1)
            
        ans.sort()
        return (ans[0] + ans[1])