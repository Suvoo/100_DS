# Famous 4sum on leetcode

def k2sum(arr,target):
    ans = []
    s = set()

    for i in range(len(arr)):
        if len(ans) == 0 or ans[-1][1] != arr[i]:
            if target - arr[i] in s:
                ans.append([target-arr[i],arr[i]])
        s.add(arr[i])
    return ans

def Ksum(arr,target,k):
    ans = []

    if not arr:
        return ans

    avg = target//k

    if arr[0] > avg or arr[-1] < avg:
        return ans
        
    # print('you have reached',k)
    if k == 2:
        return k2sum(arr,target)

    for i in range(len(arr)):
        if i == 0 or arr[i-1] != arr[i]:
            for subset in Ksum(arr[i+1:],target - arr[i],k - 1):
                ans.append([arr[i]] + subset)
    return ans

N = 6
A = [1, 5, 1, 0, 6, 0]
X = 7 # target
# o/p -> True

k = 4
A.sort()
ans = Ksum(A,X,4)
# now ans returns all possible answers
if len(ans) == 0:
    print('fail')
else:
    print('pass')


