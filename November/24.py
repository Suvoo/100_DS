n = 6
arr = [3,0,0,2,0,4]

mxl = [0] * n
mxr = [0] * n

mxl[0] = arr[0]

for i in range(1,n):
    mxl[i] = max(mxl[i-1],arr[i])

mxr[-1] = arr[-1]
for i in range(n-2,-1,-1):
    mxr[i] = max(mxr[i+1],arr[i])

ans = [0] * n
for i in range(n):
    ans[i] = min(mxl[i],mxr[i]) - arr[i]

print(sum(ans))