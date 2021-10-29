# Problem : https://practice.geeksforgeeks.org/problems/620fb6456d6515faddd77050dfbf2821d7a94b8a/1
# References : https://youtu.be/3fFTw3ixnJM
# https://discuss.codechef.com/t/number-of-minimum-picks-to-get-k-pairs-of-socks-from-a-drawer/84546/3
# great video

N = 4
K = 6
a = [3,4,5,3] # sock
# o/p --> 15
# O(n) soln
# 8
# 9 9 7 8 6 7 6 7

#calculate all pairs
pair,su = 0,0
for i in range(N):
    pair += a[i]//2
    if a[i]%2 == 0:
        su += (a[i] - 2)//2
    else:
        su += (a[i] - 1)//2
print(pair)

if pair < K:
    print(-1)
elif su >= K:
    print(2*(K-1) + (N+1))
else:
    print((2* su) + N + (K - su))



