#Problem : https://practice.geeksforgeeks.org/problems/pairs-with-specific-difference1533/1
arr = [3, 5, 10, 15, 17, 12, 9]
K = 4

arr.sort(reverse=True)
# print(arr)

i,ans = 0,0
while i < len(arr) - 1:
    # print(i)
    if arr[i] - arr[i+1] < K:
        ans += (arr[i] + arr[i+1])
        # print(arr[i],arr[i+1],ans)
        i+=1
    i+=1
print(ans)