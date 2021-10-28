# https://practice.geeksforgeeks.org/problems/number-of-unique-paths5339/1#
# Ref = on my own 😎
a = 3
b = 4

dp = [[0 for i in range(b+1)] for j in range(a+1)] # y first
# print(dp)

# base case is when there is 1x1 matrix, so all will be 1

for i in range(a+1):
    dp[i][0] = 1
for i in range(b+1):
    dp[0][i] = 1
# print(dp)

for i in range(1,a+1):
    for j in range(1,b+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] # adding both prev values

print(dp[a-1][b-1]) # ans