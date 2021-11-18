N = 2
start = [2,1]
end =  [2,2]

start = [1,3,2,5]
end =  [2,4,3,6]

arr = []
ans = 1

for i in range(len(start)):
    arr.append([start[i],end[i]])
print(arr)
arr.sort(key=lambda x: x[1])
print(arr)

j = 0
for i in range(1,len(start)):
    if arr[i][0] > arr[j][1]:
        ans+=1
        j = i
print(ans)