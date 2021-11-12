# https://www.youtube.com/watch?v=D_ZVcOVW-u0

graph = [[0,1,1,1],
        [0,0,0,1], 
        [0,0,0,1], 
        [0,0,0,0]]
u = 0
v = 3
k = 2

MOD = 1000000007
n = len(graph)
dp = [[0 for i in range(n)] for j in range(k+1)]
dp[0][u] = 1
# print(dp)

for i in range(k):
    for j in range(n):
        # print(f"{i}{j} ",end='')
        for l in range(n):
            if graph[j][l] == 1:
                dp[i+1][l] = (dp[i+1][l] + dp[i][j]) % MOD
print(dp[k][v])