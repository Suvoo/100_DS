# problem : https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

# Similar : with any sum K (aditya verma)

arr = [15,-2,2,-8,1,7,10,23]

dic = {}
dic[0] = -1
su,mx = 0,0

for i in range(len(arr)):
    su+=arr[i]

    if su in dic:
        mx = max(mx,i-dic[su])

    if su not in dic:
        dic[su] = i

print(mx)