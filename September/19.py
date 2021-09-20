# https://practice.geeksforgeeks.org/problems/median-of-2-sorted-arrays-of-different-sizes/1

import math
array1 = [1,5,9]
array2 = [2,3,6,7]

# array1 = [4,6]
# array2 = [1,2,3,5]


m = len(array1)
n = len(array2)

for i in array2:
    array1.append(i)
    
array1 = sorted(array1)
# print(array1)

if (m+n) % 2 == 0:
    ans = (array1[(m+n)//2] + array1[(m+n)//2 - 1])/ 2
else:
    ans = array1[(m+n)//2]
    
if(ans == math.floor(ans)):
    print(math.floor(ans))
else:
    print(ans)