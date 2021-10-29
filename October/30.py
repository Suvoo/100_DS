import heapq

N = 4
mat =     [
           [16, 28, 60, 64],
           [22, 41, 63, 91],
           [27, 50, 87, 93],
           [36, 78, 87, 94 ]
           ]
K = 3

#OP -> 30

a = []
for i in range(len(mat)):
    for j in range(len(mat[i])):
        # print(mat[i][j])
        a.append(mat[i][j])
# print(a)
heapq.heapify(a)

# print(a)
ans = heapq.nsmallest(K,a)
print(ans[-1])