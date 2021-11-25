n = 5
arr = [5, 3, 0, 7, 4]

arr.sort()
min1,min2 = '0','0'
for i in range(n):
    if i%2 == 0:
        min1 = min1 + str(arr[i])
    else:
        min2 = min2 + str(arr[i])
print(int(min1) + int(min2))
