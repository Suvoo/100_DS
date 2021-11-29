

# just find NSE to Right


def NSERight(arr,n):
    stack = []
    ans= [0] * n
    
    for i in range(n):

        while len(stack) != 0 and arr[stack[-1]] > arr[i]:
            ans[stack[-1]] = arr[i]
            stack.pop()

        stack.append(i)

    while len(stack) != 0:
        ans[stack[-1]] = -1
        stack.pop() 

    return ans

arr = [3, 8, 5, 2, 25]
arr = [2, 5, 3, 7, 1, 5, 2, 6, 3, 1]
# 1 3 1 1 -1 2 1 3 1 -1
ans= NSERight(arr,len(arr))
print(ans)


