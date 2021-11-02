N = 7
arr = [10,20,30,50,10,70,30]

nse_left = [-1 for i in range(len(arr))]
nse_right = [len(arr) for i in range(len(arr))]
stack = []

# fill nse_left first
    # top = stack[-1]
for i in range(len(arr)):
    while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
        stack.pop()
    if len(stack) != 0:
        nse_left[i] = stack[-1]
    stack.append(i)
# print(nse_left)
# empty stack for right
while len(stack) != 0:
    stack.pop()

# fill nse_right then
for i in range(len(arr)-1,-1,-1): 
    while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
        stack.pop()
    if len(stack) != 0:
        nse_right[i] = stack[-1]
    stack.append(i)
# print(nse_right)

ans = [0 for i in range(len(arr))]
# fill with formula
for i in range(len(arr)):
    min_window = nse_right[i] - nse_left[i] - 1
    # print(min_window)
    ans[min_window - 1] = max(ans[min_window - 1], arr[i])
print(ans)
# fill missing from formula
# done by taking max from right

for i in range(len(arr) - 1,0,-1):
    ans[i - 1] = max(ans[i - 1],ans[i])
print(ans)





