N = 4
X = 2
A = [3, 1, 2, 7]

ans = A[0]
for i in range(len(A)):
    ans =  ans & A[i]
    print(ans)
print('manlyu')
for i in A:
    print(i&X)